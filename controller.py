import view
import model

def tele_base():
    do = view.menu_action()
    if do == '1':
       res1 = view.data_read()
       if res1 == '1':
           model.read_txt()
       if res1 == '2':
           model.read_csv()
    if do == '2':
        res2 = view.data_write()
        if res2 == '1':
            info = view.get_info()
            model.write_txt(info)
        if res2 == '2':
            info = view.get_info()
            model.write_csv(info)
