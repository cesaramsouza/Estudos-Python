def master(funcao,*args,**kwargs):
    return funcao(*args,**kwargs)

def fun1(nome):
    return nome

def fun2(saudacao, padrao):
    return saudacao, padrao

exec = master(fun2,'Ola',padrao='guerreiro')
print(exec)