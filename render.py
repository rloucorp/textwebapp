from jinja2 import Template

tmpl = Template(u'''<table>
<tr>
    <td><strong>Number</strong></td> <td><strong>Square</strong></td>
</tr>
{%- for item in rows %}
<tr>
    <td>{{ item.number }}</td> <td>{{ item.square }}</td>
</tr>
{%- endfor %}
<table>
''')

data = [{"number": number, "square": number*number}
            for number in range(10)]
print tmpl.render(rows=data)
