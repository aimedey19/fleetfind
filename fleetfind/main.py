from itertools import chain

from django.db.models import Q, CharField, TextField


class FleetFindIndexMixin:
    # FIXME: Not tested yet. Just thinking of a mixin to add indexing capabilities to a model.
    """
    Mixin class for FleetFind.
    Add indexing capabilities to a model.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        indexes = [
            Index(
                lower(f"{field.name}"),
                name=f"ix_{field.name}",
            ) for field in self._meta.fields
        ]


class FleetFind(object):
    def __init__(self):
        self.search_models = {}

    def register(self, model: object, search_fields: list = None):
        """
        Register a model for search.
        :param model:
        :param search_fields:
        :return:
        """
        if search_fields:
            self.search_models[model] = search_fields
        else:
            search_fields[model] = "__all__"

    def search(self, search_query: str):
        """
        Search across multiple models.
        :param search_query:
        :return: list

        Usage:
        fleetfind("search query", {"Model1": ["field1", "field2"], "Model2": ["field3"]})

        Output:
        [
            {"id": 1, "field1": "value1", "field2": "value2"},
            {"id": 2, "field3": "value3"}

        ]
        """
        if not search_models:
            raise ValueError("search_models is empty. Please provide a dictionary of models to search.")
        search_results = []
        for search_model in search_models.keys():
            if not search_models[search_model] == "__all__":
                fields = [x for x in search_model._meta.fields if
                          (isinstance(x, CharField) or isinstance(x, TextField)) and x.name in search_models[
                              search_model]]
            else:
                # Search all charfields
                fields = [x for x in search_model._meta.fields if isinstance(x, CharField) or isinstance(x, TextField)]
            search_queries = [Q(**{x.name + "__icontains": search_query}) for x in fields]
            print(search_queries)
            q_object = Q()
            for query in search_queries:
                q_object = q_object | query

            results = search_model.objects.filter(q_object).values(*fields)
            search_results.append(results)

        return chain(*search_results)


fleetfind = FleetFind()
