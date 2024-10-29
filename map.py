from typing import Any


class DictKeyStr(dict):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        key_to_map = [key for key in self if not isinstance(key,str)]
        for key in key_to_map:
            self[str(key)] = self[key]
            del self[key]

    def __setitem__(self, key: Any, value: Any) -> None:
        return super().__setitem__(str(key), value)

    def __missing__(self,key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self,key,default=None):
        try:
            return self[key]
        except KeyError:
            return default
        
    def __contains__(self, key: object) -> bool:
        return key in self.keys() or str(key) in self.keys()
    

if __name__=='__main__':
    # Criando uma instancia de DictKeyStr
    my_dict = DictKeyStr([(1,'um'),('2','dois')])

    # Exibindo o dicionario
    print(my_dict)

    # buscando um index existente
    print(my_dict[1])

    # buscando um index existente porem com tipo diferente
    print(my_dict[2])

    # Setando um novo index
    my_dict[3] = 'tres'

    # Exibindo o dicionario completo novamente
    print(my_dict)

    # Testando __contains__
    print(2 in my_dict)
    print('1' in my_dict)

    # Testando get
    print(my_dict.get(2,None))

    # Testando o setdefault
    print(my_dict.setdefault(4,[]))