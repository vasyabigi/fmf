from sections.models import Section


def sections(request):
    sections = Section.objects.all()
    return {
        'sections': sections
    }
