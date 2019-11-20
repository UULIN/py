def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计， 知道没有未打印的设计为止
    打印每个设计后，都将其移动到completed_models中
    """
    while unprinted_designs:
        completed_model = unprinted_designs.pop()

        print("completed_model is " + completed_model)

        completed_models.append(completed_model)


def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs =['aaaa', 'vvvvv', 'cccccc']
completed_models =[]

print_models(unprinted_designs[:],completed_models)
print(unprinted_designs)
show_completed_models(completed_models)


