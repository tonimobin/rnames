from django.shortcuts import render
from rnames_app.models import (Location, Name, Qualifier, QualifierName, Reference, StructuredName)


# Create your views here.
def index(request, *args, **kwargs):
    names = list(Name.objects.filter(is_active=True).values('id', 'name'))
    locations = list(Location.objects.filter(is_active=True).values('id', 'name'))
    qualifier_names = list(QualifierName.objects.filter(is_active=True).values('id', 'name'))
    qualifiers = list(Qualifier.objects.filter(is_active=True).values('id', 'level', 'qualifier_name_id', 'stratigraphic_qualifier_id'))
    references = list(Reference.objects.filter(is_active=True).values('id', 'title', 'first_author', 'link', 'year', 'doi'))
    structured_names = list(StructuredName.objects.filter(is_active=True).values('id', 'location_id', 'name_id', 'qualifier_id', 'reference_id', 'remarks'))

    return render(request, 'frontend/index.html', {
        'names': names,
        'locations': locations,
        'qualifier_names': qualifier_names,
        'qualifiers': qualifiers,
        'references': references,
        'structured_names': structured_names
    })