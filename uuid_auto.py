import uuid


# простая генерация одного uuid вида - autotest-e201-49b1-9345-016915add803

uuid_auto = str(uuid.uuid4())
uuid_text = 'autotest'
new_uuid_auto = uuid_text + uuid_auto[8:]
print(new_uuid_auto)

# функция с циклом для генерации списка таких uuid

def get_uuid_auto():
    result = str(uuid.uuid4())
    return result



def uuid_auto(count_iter):
    uuid_text = 'autotest'
    result = []
    for _ in range(count_iter):
        new_uuid = get_uuid_auto()
        new_uuid_auto = uuid_text + new_uuid[8:]
        result.append(new_uuid_auto)
    return result

uuids_generate = uuid_auto(10)
print(uuids_generate)

