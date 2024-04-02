import xml.etree.ElementTree as ET

data = '''
<stuff>
    <users>
        <user x="2">
            <id>002</id>
            <name>Chuck</name>
        </user>
        <user x="3">
            <id>003</id>
            <name>Fer</name>
        </user>
        <user x="5">
            <id>005</id>
            <name>Pep</name>
        </user>
    </users>
</stuff>'''
x = ET.fromstring(data)
lst = x.findall('users/user')
print('User count:',len(lst))

for item in lst:
    print('NAME:',item.find('name').text)
    print('ID:',item.find('id').text)
    print('ATTR:',item.get('x'))
    print('----------')