
base_de_datos={
    "viviendas":[
    {
        "id":1,
        "direccion":"calle admin",
        "codigo_postal":"0000",
        "id_usuario":1,
    },
    {
      "id":2,
      "direccion":"calle usuario1",
      "codigo_postal":"1111",
      "id_usuario":2,
    }
    ],
    "automatizaciones":[
      {
        "id":1,
        "nombre": "Encendido de luces del Patio",
        "id_vivienda": 2, 
        "hora_inicio":"18:00",
        "hora_fin":"06:00",
        "id_dispositivo":1,
        "estado":"activo"
      } ,
      {
        "id":2,
        "nombre": "Encendido de aspiradora",
        "id_vivienda": 2, 
        "hora_inicio":"10:00",
        "hora_fin":"12:00",
        "id_dispositivo":3,
        "estado":"activo"
      }  

        
    ],
    "dispositivos":[
    {
        "id":1,
        "nombre": "luz",
        "tipo": "iluminación",
        "id_vivienda":2,
        "ubicacion": "patio",
        "estado": False,
    },
    {
        "id":2,
        "nombre": "aire acondicionado",
        "tipo": "aire acondicionado",
        "id_vivienda":2,
        "ubicacion": "habitación",
        "estado": False,
    },
    {
        "id":3,
        "nombre": "aspiradora",
        "tipo": "aspiradora",
        "id_vivienda":2,
        "ubicacion": "comedor",
        "estado": False
    }
    ],
    
    "usuarios":[
    {
        "id":1,
        "nombre":"admin",
        "contraseña":"admin",
        "correo":"admin@mail.com", 
        "Role":"admin"   
    },
    {
        "id":2,
        "nombre":"usuario1",
        "contraseña":"usuario1",
        "correo":"usuario1@mail.com",
        "Role":"estandar"
    }
    ],
    
}
