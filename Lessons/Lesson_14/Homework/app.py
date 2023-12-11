from Interfaces import FileWorker


def app():
    fw = FileWorker('test.json')
    content = fw.read()
    fw.append('obj1')
    fw.append('obj2')
    print(content)
    fw.close()


app()
