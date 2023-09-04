adjetivos = [
                "grande", "pequeño", "alto", "bajo", "gordo", "flaco", "bonito", "feo", "inteligente", "tonto",
                "bueno", "malo", "rápido", "lento", "alegre", "triste", "valiente", "cobarde", "fuerte", "débil",
                "feliz", "infeliz", "rico", "pobre", "viejo", "joven", "interesante", "aburrido", "simpático",
                "antipático",
                "divertido", "aburrido", "trabajador", "vago", "honrado", "deshonesto", "amable", "grosero", "caliente",
                "frío",
                "nuevo", "viejo", "sabio", "ignorante", "limpio", "sucio", "amoroso", "odioso", "paciente",
                "impaciente",
                "sincero", "falso", "seguro", "inseguro", "responsable", "irresponsable", "romántico", "práctico",
                "interesante", "aburrido",
                "valioso", "inútil", "educado", "maleducado", "amable", "desagradable", "rápido", "lento", "bonito",
                "feo",
                "blando", "duro", "claro", "oscuro", "alto", "bajo", "rápido", "lento", "activo", "inactivo",
                "corto", "largo", "delgado", "grueso", "amplio", "estrecho", "agradable", "desagradable", "rico",
                "pobre",
                "duro", "blando", "seco", "húmedo", "luminoso", "oscuro", "abundante", "escaso", "amargo", "dulce",
                "positivo", "negativo", "elegante", "sencillo", "difícil", "fácil", "hermoso", "feo", "amable",
                "hostil",
                "silencioso", "ruidoso", "joven", "viejo", "cálido", "frío", "atractivo", "repulsivo", "completo",
                "incompleto",
                "saludable", "enfermo", "triste", "alegre", "oscuro", "claro", "bueno", "malo", "ligero", "pesado",
                "ancho", "estrecho", "fino", "grueso", "dulce", "salado", "vacío", "lleno", "largo", "corto",
                "agudo", "grave", "rápido", "lento", "agotado", "energético", "profundo", "superficial", "verdadero",
                "falso",
                "amargo", "dulce", "triste", "alegre", "inocente", "culpable", "fácil", "difícil", "brillante", "opaco",
                "atractivo", "repulsivo", "rápido", "lento", "pequeño", "grande", "débil", "fuerte", "vivo", "muerto",
                "agradable", "desagradable", "agotador", "fácil", "difícil", "alegre", "triste", "amable", "grosero",
                "valiente",
                "cobarde", "delgado", "gordo", "bonito", "feo", "limpio", "sucio", "nuevo", "viejo", "amoroso",
                "odioso", "bueno", "malo", "sabio", "ignorante", "alegre", "triste", "rico", "pobre", "joven",
                "viejo", "alto", "bajo", "interesante", "aburrido", "simpático", "antipático", "divertido", "aburrido",
                "trabajador",
                "vago", "honrado", "deshonesto", "amable", "grosero", "caliente", "frío", "nuevo", "viejo", "sabio",
                "ignorante", "limpio", "sucio", "amoroso", "odioso", "paciente", "impaciente", "sincero", "falso",
                "seguro",
                "inseguro", "responsable", "irresponsable", "romántico", "práctico", "interesante", "aburrido",
                "valioso", "inútil", "educado",
                "maleducado", "amable", "desagradable", "rápido", "lento", "bonito", "feo", "blando", "duro", "claro",
                "oscuro", "alto", "bajo", "rápido", "lento", "activo", "inactivo", "corto", "largo", "delgado",
                "grueso", "amplio", "estrecho", "agradable", "desagradable", "rico", "pobre", "duro", "blando", "seco",
                "húmedo", "luminoso", "oscuro", "abundante", "escaso", "amargo", "dulce", "positivo", "negativo",
                "elegante",
                "sencillo", "difícil", "fácil", "hermoso", "feo", "amable", "hostil", "silencioso", "ruidoso", "joven",
                "viejo", "cálido", "frío", "atractivo", "repulsivo", "completo", "incompleto", "saludable", "enfermo",
                "triste",
                "alegre", "oscuro", "claro", "bueno", "malo", "ligero", "pesado", "ancho", "estrecho", "fino",
                "grueso", "dulce", "salado", "vacío", "lleno", "largo", "corto", "agudo", "grave", "rápido",
                "lento", "agotado", "energético", "profundo", "superficial", "verdadero", "falso", "amargo", "dulce",
                "triste",
                "alegre", "inocente", "culpable", "fácil", "difícil", "brillante", "opaco", "atractivo", "repulsivo",
                "rápido",
                "lento", "pequeño", "grande", "débil", "fuerte", "vivo", "muerto", "agradable", "desagradable",
                "agotador"]

adjetivos.sort()


temp_list = []

for i in adjetivos:
    if i not in temp_list:
        temp_list.append(i)

nexos = temp_list

print(nexos)

