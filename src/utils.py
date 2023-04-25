def update_search(text_list,new_text):
    exists = False

    for text in range(len(text_list)):
        if text_list[text] == new_text:
            exists = True
            break

    return exists