from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class PedidoForm(Form):
    nombre = StringField('nombre', [
        DataRequired(message='El nombre es requerido'),
        Length(min=4, max=50, message='El nombre debe tener entre 4 y 50 caracteres')
    ])
    
    direccion = StringField('direccion', [
        DataRequired(message='La dirección es requerida'),
        Length(min=4, max=100, message='La dirección debe tener entre 4 y 100 caracteres')
    ])
    
    telefono = StringField('telefono', [
        DataRequired(message='El teléfono es requerido'),
        Length(min=10, max=10, message='El teléfono debe tener 10 dígitos')
    ])
