from django import template

register = template.Library()

class DateRangeNode(template.Node):
    def __init__(self, start_date, end_date, format_string):
        self.start_date = template.Variable(start_date)
        self.end_date = template.Variable(end_date)
        self.format = {}
        if not len(format_string) == 0:
            format_string = format_string.encode('utf-8').strip("\"")
            self.format['day'],self.format['month'],self.format['year'] = format_string.split()
        else:
            self.format['day'],self.format['month'],self.format['year'] = "%d","%m","%Y"

    def render(self, context):
        try:
            start_date = self.start_date.resolve(context)
            end_date = self.end_date.resolve(context)
        except template.VariableDoesNotExist:
            return ''

        start_format = ""
        end_format = ""
        if start_date.day == end_date.day:
            end_format = self.format['day']
        else:
            start_format = self.format['day']
            end_format = self.format['day']

        if start_date.month == end_date.month:
            end_format += " "+self.format['month']
        else:
            start_format += " "+self.format['month']
            end_format += " "+self.format['month']

        if start_date.year == end_date.year:
            end_format += " "+self.format['year']
        else:
            start_format += " "+self.format['year']
            end_format += " "+self.format['year']
        print start_format
        print end_format

        return start_date.strftime(start_format)+" - "+end_date.strftime(end_format)

def do_date_range(parser, token):

    #{% date_range start_date end_date [format string] %}

    chunks = token.split_contents()
    if not len(chunks) >= 3:
        raise template.TemplateSyntaxError, "%r tag requires two or three arguments" % token.contents.split()[0]
    if not len(chunks) <=4 :
        raise template.TemplateSyntaxError, "%r tag requires two or three arguments" % token.contents.split()[0]
    if len(chunks) == 4:
        format = chunks[3]
    else:
        format = ""
    return DateRangeNode(chunks[1],chunks[2],format)

register.tag('date_range', do_date_range)