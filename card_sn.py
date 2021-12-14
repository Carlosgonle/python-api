card = """
{
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.2",
    "body": [
        {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "width": 2,
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "auto crea tu solicitud",
                            "weight": "Bolder",
                            "size": "Medium"
                        },
                        {
                            "type": "TextBlock",
                            "text": "con esta aplicacion podrás creas vos mismo tu propio ticket para averías.",
                            "isSubtle": true,
                            "wrap": true
                        },
                        {
                            "type": "TextBlock",
                            "text": "descripción corta",
                            "wrap": true
                        },
                        {
                            "type": "Input.Text",
                            "id": "short_description",
                            "placeholder": "descripción corta"
                        },
                        {
                            "type": "TextBlock",
                            "text": "descripción",
                            "wrap": true
                        },
                        {
                            "type": "Input.Text",
                            "id": "description",
                            "placeholder": "descripción",
                            "isMultiline": true
                        },
                        {
                            "type": "TextBlock",
                            "text": "categoria"
                        }
                    ]
                },
                {
                    "type": "Column",
                    "width": 1,
                    "items": [
                        {
                            "type": "Image",
                            "url": "https://www.silicon.es/wp-content/uploads/2020/04/servicenow300.png"
                        },
                        {
                            "type": "Image",
                            "url": "https://thumbs.dreamstime.com/z/mujer-sexy-con-sombrero-santa-chica-sensual-en-lencer%C3%ADa-er%C3%B3tica-caja-de-regalo-roja-feliz-a%C3%B1o-nuevo-navidad-perfecto-mejor-167454453.jpg",
                            "size": "auto"
                        }
                    ]
                }
            ]
        },
        {
            "type": "Input.ChoiceSet",
            "choices": [
                {
                    "title": "Choice 1",
                    "value": "Choice 1"
                },
                {
                    "title": "Choice 2",
                    "value": "Choice 2"
                }
            ],
            "placeholder": "categoria",
            "id": "category"
        }
    ],
    "actions": [
        {
            "type": "Action.Submit",
            "title": "Ingresar"
        }
    ]
}
"""