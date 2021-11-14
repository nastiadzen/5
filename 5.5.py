class АнглоРосійськийСловник():
    from translate import Translator
    a=Translator(from_lang="english",to_lang="russian")
    b=a.translate(input("Введіть слово "))
    print(b)