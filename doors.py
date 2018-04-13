doors = []
ind = 1
for ind in range(1, 101):
    doors.append({'key': ind, 'status': 'closed'})
    ind += 1

i = 1
add = 1


def open_doors(doors, i):
    for val in doors:
        if val['key'] in range(0, 101, i):
            print(val['key'])
            if val['status'] == 'closed':
                val['status'] = 'open'

            elif val['status'] == 'open':
                val['status'] = 'closed'

            print(val['status'])


while i in range(1, 101):
    open_doors(doors, i)
    i += 1

print('-----')

for val in doors:
    print(val['key'], ', ', val['status'])

# following doors are open: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
