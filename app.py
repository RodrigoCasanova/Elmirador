from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from flask_cors import CORS

app = Flask(__name__)

# Configuración y credenciales de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:duoc@localhost/elmirador'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy(app)

# Modelo Departamento
class Departamento(db.Model):
    CodDepto = db.Column(db.String(10), primary_key=True)  # Código único del departamento
    Piso = db.Column(db.String(10), nullable=False)        # Piso del departamento
    Numero = db.Column(db.String(10), nullable=False)      # Número del departamento
    Arrendado = db.Column(db.Boolean, default=False)       # Si está arrendado o no
    RutProp = db.Column(db.String(12), nullable=False)     # RUT del propietario
    Estado = db.Column(db.String(20), nullable=False)      # Estado del departamento
    RutArre = db.Column(db.String(12), nullable=True)      # RUT del arrendatario
    FechaIniC = db.Column(db.String(10), nullable=True)    # Fecha de inicio del contrato
    FechaFinC = db.Column(db.String(10), nullable=True)    # Fecha de fin del contrato
    Observacion = db.Column(db.String(200), nullable=True) # Observaciones adicionales
    NumHab = db.Column(db.Integer, nullable=False)         # Número de habitaciones
    NumBaños = db.Column(db.Integer, nullable=False)       # Número de baños

# Modelo GastoComun
class GastoComun(db.Model):
    id_cuota_gc = db.Column(db.Integer, primary_key=True)  # Llave primaria
    mes = db.Column(db.String(2), nullable=False)          # Mes del gasto
    anio = db.Column(db.String(4), nullable=False)         # Año del gasto
    valor_pagado = db.Column(db.Float, default=0.0)        # Valor pagado
    fecha_pago = db.Column(db.String(10), nullable=True)   # Fecha de pago
    atrasado = db.Column(db.Boolean, default=False)        # Si está atrasado o no
    cod_depto = db.Column(db.String(10), db.ForeignKey('departamento.CodDepto'), nullable=False)  # Relación con Departamento
    rut = db.Column(db.String(12), nullable=True)          # RUT del pagador
    nombre = db.Column(db.String(100), nullable=True)      # Nombre del pagador
    telefono = db.Column(db.String(15), nullable=True)     # Teléfono del pagador

    departamento = db.relationship('Departamento', backref=db.backref('gastos_comunes', lazy=True))

# Crear la base de datos y las tablas si no existen
with app.app_context():
    db.create_all()

@app.route('/crear_gastos_comunes', methods=['POST'])
def crear_gastos_comunes():
    """
    Crea los gastos comunes para todos los departamentos en un mes y año determinados.
    """
    data = request.get_json()
    mes = data.get('mes')
    anio = data.get('anio')

    if not mes or not anio:
        return jsonify({'error': 'Mes y Año son requeridos'}), 400

    # Obtener todos los departamentos
    departamentos = Departamento.query.all()

    # Crear un gasto común para cada departamento
    for departamento in departamentos:
        nuevo_gasto = GastoComun(
            mes=mes,
            anio=anio,
            cod_depto=departamento.CodDepto,
            valor_pagado=0.0,  # Valor por defecto
            fecha_pago=None,   # Por defecto no hay fecha de pago
            atrasado=False,    # Se marca como no atrasado por defecto
            rut=None,          # No se asigna RUT al inicio
            nombre=None,       # No se asigna nombre
            telefono=None      # No se asigna teléfono
        )
        db.session.add(nuevo_gasto)

    db.session.commit()

    return jsonify({'mensaje': 'Gastos comunes creados exitosamente'}), 201


@app.route('/gastos_comunes', methods=['GET'])
def obtener_gastos_comunes():
    """
    Obtiene todos los gastos comunes registrados.
    """
    gastos = GastoComun.query.all()
    return jsonify([{
        'id': gasto.id_cuota_gc,
        'anio': gasto.anio,
        'mes': gasto.mes,
        'valor_pagado': gasto.valor_pagado,
        'fecha_pago': gasto.fecha_pago,
        'atrasado': gasto.atrasado,
        'cod_depto': gasto.cod_depto,
        'rut': gasto.rut,
        'nombre': gasto.nombre,
        'telefono': gasto.telefono
    } for gasto in gastos])

@app.route('/crear_departamentos', methods=['POST'])
def crear_departamentos():
    departamentos = [
        Departamento(CodDepto='A101', Piso='1', Numero='01', Arrendado=False, RutProp='11111111-1', Estado='Disponible', RutArre=None, FechaIniC=None, FechaFinC=None, Observacion=None, NumHab=3, NumBaños=2),
        Departamento(CodDepto='A102', Piso='1', Numero='02', Arrendado=False, RutProp='22222222-2', Estado='Disponible', RutArre=None, FechaIniC=None, FechaFinC=None, Observacion=None, NumHab=2, NumBaños=1),
        Departamento(CodDepto='A103', Piso='1', Numero='03', Arrendado=True, RutProp='33333333-3', Estado='Arrendado', RutArre='44444444-4', FechaIniC='01-01-2021', FechaFinC='01-01-2022', Observacion='Contrato renovado', NumHab=1, NumBaños=1),
        Departamento(CodDepto='A201', Piso='2', Numero='01', Arrendado=False, RutProp='55555555-5', Estado='Disponible', RutArre=None, FechaIniC=None, FechaFinC=None, Observacion=None, NumHab=3, NumBaños=2),
        Departamento(CodDepto='A202', Piso='2', Numero='02', Arrendado=False, RutProp='66666666-6', Estado='Disponible', RutArre=None, FechaIniC=None, FechaFinC=None, Observacion=None, NumHab=2, NumBaños=1),
        Departamento(CodDepto='A203', Piso='2', Numero='03', Arrendado=True, RutProp='77777777-7', Estado='Arrendado', RutArre='88888888-8', FechaIniC='01-01-2021', FechaFinC='01-01-2022', Observacion='Contrato renovado', NumHab=1, NumBaños=1)
    ]
    db.session.add_all(departamentos)
    db.session.commit()
    return jsonify({'mensaje': 'Departamentos creados exitosamente'}), 201


@app.route('/listar_departamentos', methods=['GET'])
def listar_departamentos():
    """
    Listar todos los departamentos registrados.
    """
    # Obtener todos los departamentos de la base de datos
    departamentos = Departamento.query.all()

    # Si no se encuentran departamentos, devolver mensaje
    if not departamentos:
        return jsonify({'mensaje': 'No hay departamentos registrados'}), 200

    # Formatear la lista de departamentos para la respuesta
    lista_departamentos = []
    for departamento in departamentos:
        lista_departamentos.append({
            'CodDepto': departamento.CodDepto,
            'Piso': departamento.Piso,
            'Numero': departamento.Numero,
            'Arrendado': departamento.Arrendado,
            'RutProp': departamento.RutProp,
            'Estado': departamento.Estado,
            'RutArre': departamento.RutArre,
            'FechaIniC': departamento.FechaIniC,
            'FechaFinC': departamento.FechaFinC,
            'Observacion': departamento.Observacion,
            'NumHab': departamento.NumHab,
            'NumBaños': departamento.NumBaños
        })

    return jsonify({'departamentos': lista_departamentos}), 200


@app.route('/marcar_como_pagado', methods=['POST'])
def marcar_como_pagado():
    """
    Marca el pago de un gasto común como realizado, determinando si es dentro de plazo, fuera de plazo o duplicado.
    Requiere los campos: CodDepto, mes, anio, fecha_pago.
    """
    data = request.get_json()

    # Validar que los campos requeridos estén presentes
    if 'CodDepto' not in data or 'mes' not in data or 'anio' not in data or 'fecha_pago' not in data:
        return jsonify({'error': 'Campos CodDepto, mes, anio, y fecha_pago son requeridos'}), 400

    # Buscar el departamento correspondiente
    departamento = Departamento.query.filter_by(CodDepto=data['CodDepto']).first()
    if not departamento:
        return jsonify({'error': 'Departamento no encontrado'}), 404

    # Buscar el gasto común correspondiente
    gasto = GastoComun.query.filter_by(cod_depto=data['CodDepto'], mes=data['mes'], anio=data['anio']).first()
    if not gasto:
        return jsonify({'error': 'Gasto común no encontrado para el departamento y periodo especificado'}), 404

    # Verificar si ya se ha registrado un pago previamente
    if gasto.fecha_pago:
        return jsonify({'mensaje': 'Pago duplicado'}), 400

    # Procesar la fecha de pago
    fecha_pago = datetime.strptime(data['fecha_pago'], '%Y-%m-%d')  # Formato esperado: 'YYYY-MM-DD'
    fecha_limite = datetime.strptime(f"{data['anio']}-{data['mes']}-01", '%Y-%m-%d')
    # Ajustar fecha límite al último día del mes
    fecha_limite = fecha_limite.replace(day=28) + timedelta(days=4)  # Esto asegura que obtenemos el último día del mes
    fecha_limite = fecha_limite - timedelta(days=fecha_limite.day)

    # Verificar si el pago fue realizado dentro del plazo
    if fecha_pago <= fecha_limite:
        estado_pago = "Pago exitoso dentro del plazo"
        atraso = False
    else:
        estado_pago = "Pago exitoso fuera de plazo"
        atraso = True

    # Actualizar los datos del gasto común
    gasto.fecha_pago = data['fecha_pago']
    gasto.atrasado = atraso

    # Guardar cambios en la base de datos
    db.session.commit()

    # Devolver la respuesta
    return jsonify({
        'mensaje': estado_pago,
        'departamento': data['CodDepto'],
        'fecha_pago': data['fecha_pago'],
        'periodo': f"{data['mes']}/{data['anio']}"
    }), 200


@app.route('/listar_gastos_pendientes', methods=['POST'])
def listar_gastos_pendientes():
    """
    Listar los gastos comunes pendientes de pago desde enero hasta el mes en curso del año indicado.
    Recibe un JSON con los parámetros 'mes' y 'anio'.
    Si no hay montos pendientes, se devuelve el mensaje 'Sin montos pendientes'.
    """
    # Obtener los parámetros mes y anio del cuerpo de la solicitud en formato JSON
    data = request.get_json()

    # Verificar si los parámetros 'mes' y 'anio' están presentes en el JSON
    if not data or 'mes' not in data or 'anio' not in data:
        return jsonify({'error': 'Se requiere mes y año como parámetros en el cuerpo de la solicitud'}), 400

    mes = data['mes']
    anio = data['anio']

    # Validar que mes y anio sean números válidos
    if not isinstance(mes, int) or not isinstance(anio, int):
        return jsonify({'error': 'El mes y año deben ser valores numéricos'}), 400

    # Validar que el mes esté dentro del rango permitido (1-12)
    if mes < 1 or mes > 12:
        return jsonify({'error': 'El mes debe estar entre 1 y 12'}), 400

    # Buscar los gastos comunes pendientes de pago
    gastos_pendientes = GastoComun.query.filter(
        GastoComun.anio <= anio,
        (GastoComun.anio < anio) | (GastoComun.mes <= mes),
        GastoComun.fecha_pago == None  # Solo los gastos sin pago registrado
    ).all()

    if not gastos_pendientes:
        return jsonify({'mensaje': 'Sin montos pendientes'}), 200

    # Formato de respuesta: Lista de gastos pendientes
    lista_gastos = []
    for gasto in gastos_pendientes:
        lista_gastos.append({
            'CodDepto': gasto.cod_depto,
            'Mes': gasto.mes,
            'Anio': gasto.anio,
            'ValorPagado': gasto.valor_pagado,
            'FechaPago': gasto.fecha_pago,
            'Atrasado': gasto.atrasado
        })

    return jsonify({'gastos_pendientes': lista_gastos}), 200    



if __name__ == '__main__':
    app.run(debug=True)
