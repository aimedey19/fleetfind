from itertools import chain

from django.db.models import Q, CharField, TextField

def fleetfind(search_query: str = None, models: dict = None):
    search_models = models
    if not search_models:
        raise ValueError("search_models is empty. Please provide a dictionary of models to search.")
    search_results = []
    for search_model in search_models.keys():
        if not search_models[search_model] == "__all__":
            fields = [x for x in search_model._meta.fields if (isinstance(x, CharField) or isinstance(x, TextField)) and x.name in search_models[search_model]]
        else:
            # Search all charfields
            fields = [x for x in search_model._meta.fields if isinstance(x, CharField) or isinstance(x, TextField)]
        search_queries = [Q(**{x.name + "__icontains": search_query}) for x in fields]
        print(search_queries)
        q_object = Q()
        for query in search_queries:
            q_object = q_object | query

        results = search_model.objects.filter(q_object)
        search_results.append(results)

    return chain(*search_results)
