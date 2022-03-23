def post_category(test_client, input, s_code, added_categories_ids: list):
    if s_code == 201:
        added_categories_ids.append(1)
    print(f"post: {test_client = } {input = } {s_code = } {added_categories_ids = }")


def put_category(test_client, id, input, s_code):
    print(f"put: {test_client = } {id = } {input = } {s_code = }")


def delete_category(test_client, added_categories_ids: list):
    del added_categories_ids[0]
    print(f"del: {test_client = } {added_categories_ids = }")


def test_category_crud(test_client):
    client = test_client
    added_categories_ids = list()
    post_parametrize = [
        ['input', 's_code'],
        [
            [dict(name="test category"), 201],
            [dict(name="test category2"), 201],
            [dict(namex=""), 422]
        ]
    ]
    for i in range(len(post_parametrize[1])):
        post_category(
            test_client=client,
            input=post_parametrize[1][i][0],
            s_code=post_parametrize[1][i][1],
            added_categories_ids=added_categories_ids
        )
    print(f"after post {added_categories_ids=}")

    put_parametrize = [
        ['id', 'input', 's_code'],
        [
            [added_categories_ids[0], dict(name="new test category"), 200],
            [added_categories_ids[1], dict(name="new test category2"), 200],
            [10, dict(namex="a"), 422],
            [987456, dict(name="new test category3"), 404]
        ]
    ]
    for i in range(len(put_parametrize[1])):
        put_category(
            test_client=client,
            id=put_parametrize[1][i][0],
            input=put_parametrize[1][i][1],
            s_code=put_parametrize[1][i][2]
        )

    print(f"after put {added_categories_ids=}")

    for i in range(len(added_categories_ids)):
        delete_category(client, added_categories_ids)

    print(f"after del {added_categories_ids=}")


test_category_crud(0)
