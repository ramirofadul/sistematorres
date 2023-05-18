from django.db import models
from django.utils import timezone


from apps.base.models import BaseModel

# Create your models here.
#--------- Sección PARTES - JUICIOS ----------------------
class TiposProcesos(BaseModel):
    txProceso = models.CharField('Proceso', max_length=30, blank=False, null=False, unique=True)
    txDescripcion = models.CharField('Descripción',max_length=150, blank=True,null=True)

    class Meta:
        verbose_name = 'Proceso'
        verbose_name_plural = 'Procesos'
        ordering = ['txProceso']

    def __str__(self):
        """
        String que representa al objeto
        """
        return self.txProceso

class TipoFinJuicios(BaseModel):
    txTipoFin = models.CharField('Tipo Fin',max_length=30, blank=False, null=False, unique=True)
    txDescripcion = models.CharField('Descripción',max_length=150, blank=True, null=True)

    class Meta:
        ordering = ['txTipoFin']
        verbose_name='TipoFin'
        verbose_name_plural='TipoFinJuicios'
    def __str__(self):
        """
        String que representa al objeto
        """
        return self.txTipoFin

class SubTipoFinJuicios(BaseModel):
    txSubTipoFin = models.CharField('SubTipo Fin',max_length = 30, blank=False, null=False, unique=True)
    txDescripcion = models.CharField('Descripción',max_length=150, blank=True, null=True)
    idTipoFin = models.ForeignKey(TipoFinJuicios, on_delete=models.CASCADE, verbose_name='SubTipo Fin')

    class Meta:
        ordering = ['txSubTipoFin']
        verbose_name='SubTipoFin'
        verbose_name_plural='SubTipoFinJuicios'
    def __str__(self):
        """
        String que representa al objeto
        """
        return self.txSubTipoFin

class UbicacionesCarpetas(BaseModel):
    txUbicacion = models.CharField('Ubicación',max_length=30, blank=False, null=False, unique=True)
    txDescripcion = models.CharField('Descripción',max_length=150, blank=True, null=True)

    class Meta:
        ordering = ['txUbicacion']
        verbose_name='Ubicacion'
        verbose_name_plural='Ubicaciones'

    def __str__(self):
        """
        String que representa al objeto
        """
        return self.txUbicacion


class TipoCarpetas(BaseModel):
    txTipoCarpeta = models.CharField('Tipo Carpeta',max_length=30, blank=False, null=False, unique=True)
    txDescripcion = models.CharField('Descripción',max_length=150, blank=True, null=True)

    class Meta:
        ordering = ['txTipoCarpeta']
        verbose_name='TipoCarpeta'
        verbose_name_plural='TipoCarpetas'
    def __str__(self):
        """
        String que representa al objeto
        """
        return self.txTipoCarpeta

class NaturalezaJuicio(BaseModel):
    txNaturaleza = models.CharField('Naturaleza',max_length=30,blank=False, null=False, unique=True)
    txDescripcion = models.CharField('Descripción',max_length=150,blank=True,null=True)

    class Meta:
        ordering = ['txNaturaleza']
        verbose_name='Naturaleza'
        verbose_name_plural='Naturalezas'

    def __str__(self):
        """
        String que representa al objeto
        """
        return self.txNaturaleza

class EstadosCarpetas(BaseModel):
    txEstadoCarpeta = models.CharField('Estado Carpeta',max_length=30, blank=False,null=False,unique=True)
    txDescripcion = models.CharField('Descripción',max_length=150, blank=True, null=True)

    class Meta:
        ordering = ['txEstadoCarpeta']
        verbose_name='EstadoCarpeta'
        verbose_name_plural='EstadosCarpetas'
    def __str__(self):
        """
        String que representa al objeto
        """
        return self.txEstadoCarpeta

class Configuraciones(BaseModel):
    txVariable = models.CharField('Variable',max_length=30, blank=False,null=False, unique=True)
    nuValor = models.DecimalField('Valor',max_digits = 8, decimal_places = 2, blank=True, null=True)
    txDescripcion = models.CharField('Descripción',max_length=150)

    class Meta:
        ordering = ['txVariable']
        verbose_name='Variable'
        verbose_name_plural='Variables'

    def __str__(self):
        """
        String que representa al objeto
        """
        return self.txVariable

class EstadosProcesales(BaseModel):
    txEstadoProcesal = models.CharField('Estado Procesal',max_length=25, blank=False, null=False, unique=True)
    txDescripcion = models.CharField('Descripción',max_length=150, blank=True, null=True)
    idTipoProcesoId = models.ForeignKey(TiposProcesos, models.SET_NULL, blank=True, null=True, verbose_name='Tipo Proceso')
    nuOrden = models.IntegerField()

    class Meta:
        verbose_name = 'EstadoProcesal'
        verbose_name_plural ='EstadosProcesales'
        ordering = ['nuOrden']
    def __str__(self):
            """
            String que representa al objeto
            """
            return self.txEstadoProcesal


#-------------Sección LOCALIDADES Y PROVINCIAS -------------------------------------
class Paises(BaseModel):
    txPais = models.CharField('País',max_length=150, blank=False, null=False, unique=True)
    class Meta:
        ordering = ['txPais']
        verbose_name='Pais'
        verbose_name_plural='Paises'

    def __str__(self):
        """
        String que representa al objeto
        """
        return self.txPais

class Provincias(BaseModel):
    txProvincia = models.CharField('Provincia',max_length=150, blank=False, null=False, unique=True)
    idPais = models.ForeignKey(Paises, models.SET_NULL, blank=True, null=True, verbose_name='Pais')
    
    class Meta:
        ordering = ['txProvincia']
        verbose_name='Provincia'
        verbose_name_plural='Provincias'

    def __str__(self):
        """
        String que representa al objeto
        """
        return self.txProvincia


class Localidades(BaseModel):
    txLocalidad = models.CharField('Localidad',max_length=150, blank=False, null=False, unique=True)
    idProvincia = models.ForeignKey(Provincias, models.SET_NULL, blank=True, null=True,verbose_name='Provincia')

    class Meta:
        ordering = ['txLocalidad']
        verbose_name='Localidad'
        verbose_name_plural='Localidades'

    def __str__(self):
        """
        String que representa al objeto
        """
        return self.txLocalidad

#------------Sección Siniestros ---------------------------------
class TipoSiniestro(BaseModel):
    txTipoSiniestro = models.CharField('Tipo Siniestro',max_length=50, blank=False, null=False, unique=True)
    txDescripcion = models.CharField('Descripción',max_length=300, blank=True, null=True)

    class Meta:
        ordering = ['txTipoSiniestro']
        verbose_name='Tipo Siniestro'
        verbose_name_plural='Tipos Siniestros'

    def __str__(self):
        """
        String que representa al objeto
        """
        return self.txTipoSiniestro

class EnfermedadReclamada(BaseModel):
    txEnfermedadReclamada = models.CharField('Enfermedad Reclamada',max_length=300, blank=False,null=False, unique=True)
    flListada = models.BooleanField(default = False)

    class Meta:
        ordering = ['txEnfermedadReclamada']
        verbose_name='Enfermedad Reclamada'
        verbose_name_plural='Enfermedades Reclamadas'

    def __str__(self):
        """
        String que representa al objeto
        """
        return self.txEnfermedadReclamada

class Siniestros(BaseModel):
    txDescripcion = models.CharField('Descripción',max_length=300, blank=True, null=True)
    idTipoSiniestro = models.ForeignKey(TipoSiniestro, on_delete=models.CASCADE, verbose_name='Tipo Siniestro')
    nuPorcentaje = models.DecimalField('Porcentaje',max_digits = 5, decimal_places = 2, null=True)
    fcFechaSiniestro = models.DateTimeField('Fecha Siniestro',null=True,blank=True)
    idEnfermedadReclamada = models.ForeignKey(EnfermedadReclamada, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Enfermedad Reclamada')
    fcFechaSiniestroPMI = models.DateTimeField('Fecha Siniestro PMI',null=True,blank=True)
    nuEdadEmpleado = models.IntegerField()

    class Meta:
        ordering = ['txDescripcion']
        verbose_name='Siniestro'
        verbose_name_plural='Siniestros'

    def __str__(self):
        """
        String que representa al objeto
        """
        return self.id


#-------------------------Mandatarias----------------------------------
class Mandatarias(BaseModel):
    txNombre = models.CharField('Nombre',max_length=100, blank=False, null=False, unique=True)

    class Meta:
        ordering = ['txNombre']
        verbose_name='Mandataria'
        verbose_name_plural='Mandatarias'

    def __str__(self):
        """
        String que representa al objeto
        """
        return self.txNombre

#----------------------Cuentas Bancarias ---------------------------
class EstadoCuentaBancaria(BaseModel):
    txEstadoCuentaBancaria = models.CharField('Estado Cuenta Bancaria',max_length=50, blank=False, null=False, unique=True)
    txDescripcion = models.CharField('Descripción',max_length=250, blank=True, null=True)

    class Meta:
        ordering = ['txEstadoCuentaBancaria']
        verbose_name='Estado Cuenta Bancaria'
        verbose_name_plural='Estados Cuentas Bancarias'

    def __str__(self):
        """
        String que representa al objeto
        """
        return self.txEstadoCuentaBancaria

class CuentasBancarias(BaseModel):
    nuSucursal = models.IntegerField('Sucursal')
    nuNroCuenta = models.IntegerField('Nro de Cuenta')
    nuCbu = models.IntegerField('CBU', blank=False, null=False, unique=True)
    idEstadoCuentaBancaria = models.ForeignKey(EstadoCuentaBancaria, on_delete=models.CASCADE, verbose_name='Estado Cuenta Bancaria')
    fcFechaSolicitud = models.DateTimeField('Fecha Solicitud',blank=True,null=True)
    fcFechaEnvioNota = models.DateTimeField('Fecha Envío Nota',blank=True,null=True)
    fcFechaApertura = models.DateTimeField('Fecha Apertura',blank=True,null=True)

    class Meta:
        ordering = ['nuCbu']
        verbose_name='Cuenta Bancaria'
        verbose_name_plural='Cuentas Bancarias'

    def __str__(self):
        """
        String que representa al objeto
        """
        return self.nuCbu

#-----Sección Abogados --------------------------------------------
class TipoRelacionAbogado(BaseModel):
    txTipoRelacion = models.CharField('Tipo de Relación',max_length=50, blank=False, null=False, unique=True)
    txDescripcion = models.CharField('Descripción',max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['txTipoRelacion']
        verbose_name='Tipo de Relacion'
        verbose_name_plural='Tipos de Relaciones'

    def __str__(self):
        """
        String que representa al objeto
        """
        return self.txTipoRelacion


class Abogados(BaseModel):
    txNombres = models.CharField('Nombres',max_length=100, blank=False, null=False)
    txApellidos = models.CharField('Apellidos',max_length=100, blank=False, null=False)
    nuDNI = models.IntegerField('DNI',help_text="Escribir los 8 dígitos del DNI, sin puntos, por ejemplo '31921996'", null=True, blank=True, unique=True)
    txMatricula = models.CharField('Matrícula',max_length=50, null=True, blank=True, unique=True)
    txDireccion = models.CharField('Dirección',max_length=200, null=True, blank=True,)
    idLocalidad = models.ForeignKey(Localidades, on_delete=models.RESTRICT, null=True, blank=True)
    idProvincia = models.ForeignKey(Provincias, on_delete=models.RESTRICT, null=True, blank=True)
    txTelefono = models.CharField('Teléfono',max_length=20, null=True, blank=True,)
    txMail = models.EmailField('Mail',max_length=254, null=True, blank=True)
    arFoto = models.ImageField('Foto',upload_to=None, height_field=None, width_field=None, max_length=100, null=True, blank=True,)
    txObservaciones = models.TextField('Observaciones',max_length=None, null=True, blank=True,)
    flPerteneceEstudio = models.BooleanField('Pertenece al Estudio',default = False, blank=False,)
    flFacturaconIVA = models.BooleanField('Factura con IVA', default= False, blank=False)
    txNombreUsuario = models.CharField('Nombre Usuario',help_text='Usuario para el SAC',max_length=100, blank=True, null=True)
    flAtiendeInterior= models.BooleanField('Corresponsal', help_text='Es corresponsal?', default=False, blank=False)
    psClaveSac = models.CharField('Clave SAC',max_length=100, blank=True, null=True)
    rlJuiciosAbogados = models.ManyToManyField('Juicios', through='JuiciosAbogados')
 
    class Meta:
        verbose_name = 'Abogado'
        verbose_name_plural ='Abogados'
        ordering = ['txApellidos', 'txNombres']

    def __str__(self):
        """
        String que representa al objeto
        """
        txNombreCompleto = str(self.txApellidos) + ' ' + str(self.txNombres)

        return txNombreCompleto

class JuiciosAbogados(BaseModel):
    idJuicio = models.ForeignKey('Juicios', on_delete=models.CASCADE, blank=False, null=False, verbose_name='Juicio')
    idAbogado = models.ForeignKey(Abogados, on_delete=models.CASCADE, verbose_name='Abogado')
    fcFechaComparece =  models.DateTimeField('Fecha Comparece',null=True,help_text="Fecha de ingreso demanda o del comparendo",blank=True)
    fcFechaRenuncia =  models.DateTimeField('Fecha Renuncia',null=True, help_text="Fecha de renuncia", blank=True,)
    idTipoRelacionAbogado = models.ForeignKey(TipoRelacionAbogado, models.SET_NULL, blank=True, null=True,)

    class Meta:
        ordering = ['idJuicio']
        verbose_name='Juicio Abogado'
        verbose_name_plural='Juicios Abogados'

    def __str__(self):
        """
        String que representa al objeto
        """
        return self.idJuicio

#-------------Sección JUICIO -------------------------------------

class Juicios(BaseModel):
    # Campos
    fcFechaInicio = models.DateField('Fecha Inicio',default=timezone.now, help_text="Fecha de presentación de la demanda", null=False, blank=False)
    fcFechaFin = models.DateField('Fecha Fin',blank=True, null=True)
    fcFechaDerivacion = models.DateField('Fecha Derivación',default=timezone.now, help_text="Fecha del mail de derivación de la causa", null=True, blank=True)
    idTipoProceso = models.ForeignKey(TiposProcesos, models.SET_NULL, blank=True, null=True, verbose_name='Tipo Proceso')
    idEstadoProcesal = models.ForeignKey(EstadosProcesales, models.SET_NULL, blank=True, null=True, verbose_name='Estado Procesal')
    idTipoFinJuicio = models.ForeignKey(TipoFinJuicios, models.SET_NULL, blank=True, null=True, verbose_name='Tipo Fin Juicio')
    idNaturaleza = models.ForeignKey(NaturalezaJuicio, models.SET_NULL, blank=True, null=True, verbose_name='Naturaleza Juicio')
    idSiniestro = models.ForeignKey(Siniestros, models.SET_NULL, blank=True, null=True,verbose_name='Siniestro')
    idMandataria = models.ForeignKey(Mandatarias, models.SET_NULL, blank=True, null=True,verbose_name='Mandataria')
    idAbogAdministrador = models.ForeignKey(Abogados, models.SET_NULL, blank=True, null=True,related_name='Abogado_Administrador', limit_choices_to={'flPerteneceEstudio': True},)
    idAbogAdministradorAnterior = models.ForeignKey(Abogados, models.SET_NULL, blank=True, null=True,related_name='Abogado_Administrador_Anterior',limit_choices_to={'flPerteneceEstudio': True},)
    idAbogCorresponsal = models.ForeignKey(Abogados, models.SET_NULL, blank=True, null=True,related_name='corresponsal',limit_choices_to={'flAtiendeInterior': True},)
    idEstadoCarpeta = models.ForeignKey(EstadosCarpetas, models.SET_NULL, blank=True, null=True,)
    idSubTipoFinJuicio = models.ForeignKey(SubTipoFinJuicios, models.SET_NULL, blank=True, null=True,)
    idCuentaBancaria = models.ForeignKey(CuentasBancarias, models.SET_NULL, blank=True, null=True,)
    idTipoCarpeta = models.ForeignKey(TipoCarpetas, models.SET_NULL, blank=True, null=True,)
    idUbicacionCarpeta = models.ForeignKey(UbicacionesCarpetas, models.SET_NULL, blank=True, null=True,)
    txCaratula = models.CharField('Carátula',max_length=150, blank=False, null=False,)
    txNumeroExpediente = models.CharField('Número de Expediente',max_length=15, null=True, blank=True)
    txNumeroSiniestroMandataria = models.CharField('Nro Siniestro Mandataria',max_length=15, null=True, blank=True)
    txNumeroJuicioMandataria = models.CharField('Nro Juicio Mandataria',max_length=15, null=True, blank=True)
    txCargadopor = models.ForeignKey("users.User", on_delete=models.CASCADE)
    txObservaciones = models.TextField('Observaciones',max_length=150, blank=True, null=True,)
    txVersion = models.CharField('Versión',max_length=150, blank=True, null=True,)
    txNroTramite = models.CharField('Nro Tramite',max_length=150, blank=True, null=True,)
    txNroExpedienteViejo = models.CharField('Nro Expediente Viejo',max_length=150, blank=True, null=True,)
    nuMontoDemanda = models.DecimalField('Monto Demanda',max_digits = 12, decimal_places = 2, blank=True, null=True,)
    
    class Meta:
        verbose_name = 'Juicio'
        verbose_name_plural = 'Juicios'
        ordering = ['id']

    def __str__(self):
            """
            String que representa al objeto
            """
            return self.txCaratula

#----------------------Movimientos ---------------------------
class TipoMovimiento(BaseModel):
    txNombre = models.CharField('Tipo Movimiento',max_length=50, blank=False, null=False, unique=True)
    txDescripcion = models.CharField('Descripción',max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = 'Tipo Movimiento'
        verbose_name_plural = 'Tipos Movimientos'
        ordering = ['txNombre']

    def __str__(self):
            """
            String que representa al objeto
            """
            return self.txNombre



class Movimientos(BaseModel):
    idTipoMovimiento = models.ForeignKey(TipoMovimiento, on_delete=models.CASCADE, blank=False, null=False)
    txMovimiento = models.CharField('Movimiento',max_length=1000, blank=False, null=False)
    idJuicio = models.ForeignKey(Juicios, on_delete=models.PROTECT, verbose_name='Juicio', blank=False, null=False)
    iduser = models.ForeignKey("users.User", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
        ordering = ['idJuicio']

    def __str__(self):
            """
            String que representa al objeto
            """
            return self.idJuicio

 