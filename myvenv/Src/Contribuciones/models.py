from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete


class tipo_proyecto(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:

        verbose_name = 'tipo_proyecto'
        verbose_name_plural = 'tipo_proyectos'
    
    def __str__(self):
        return self.nombre

class   persona(models.Model):

    nombre_persona = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    DPI = models.CharField(max_length=16)
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=75)
    telefono = models.CharField(max_length=20)

    class Meta:

        verbose_name = 'persona'
        verbose_name_plural = 'personas'
    
    def __str__(self):
        return self.nombre_persona

class cuenta(models.Model):
    """Model definition for cuenta."""
    fecha = models.DateField()
    total = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    estado = models.BooleanField(blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    area = models.CharField(max_length=100)
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    saldo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    nombre_persona = models.ForeignKey(persona,on_delete= models.PROTECT)

    # def update_saldo(self):
    #     producto = self.detalle_set.all()
    #     for prod in producto:
    #         saldo -= prod.cantidad
    #     self.saldo = saldo
    #     self.save()

    class Meta:
        """Meta definition for cuenta."""

        verbose_name = 'cuenta'
        verbose_name_plural = 'cuentas'

    def __str__(self):
        return str(self.nombre_persona)
        
    
   


class proyecto(models.Model):
    """Model definition for factura."""

    nombre= models.CharField(max_length=300)
    ubicacion= models.CharField(max_length=150)
    descripcion=models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tipo_proyecto = models.ForeignKey(tipo_proyecto,on_delete= models.PROTECT)
    
    
    # def get_absolute_url(self):
    #     return u'/tienda/facturas/%d' % self.id 


    class Meta:
        """Meta definition for factura."""

        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'

    def __str__(self):
        return str(self.id)

class abono(models.Model):
    fecha = models.DateField()
    cantidad = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0)
    cuenta = models.ForeignKey(cuenta,on_delete= models.PROTECT)

    class Meta:
        """Meta definition for detalle."""

        verbose_name = 'abono'
        verbose_name_plural = 'abonos'

    def __str__(self):
        return str(self.id)

class detalle(models.Model):
    """Model definition for detalle."""
    
    cuenta = models.ForeignKey(cuenta,on_delete= models.PROTECT)
    proyecto = models.ForeignKey(proyecto,on_delete= models.PROTECT)

    class Meta:
        """Meta definition for detalle."""

        verbose_name = 'detalle'
        verbose_name_plural = 'detalles'

    def __str__(self):
        return str(self.id)


# def detalle_pre_save_receiver(sender, instance, *args, **kwargs):
#  """Pre saves the price and subtotal of orders."""
# #     cant = instance.cantidad
# #     if cant >= 1:
# #         precio = instance.producto.precio
# #         subtotal = cant * precio
# #         instance.precio = precio
# #         instance.subtotal = subtotal


# pre_save.connect(detalle_pre_save_receiver, sender=abono)

# def detalle_post_save_receiver(sender, instance, *args, **kwargs):
#     """Calls update_total def from Order Model"""
#      instance.cuenta.update_saldo()

# post_save.connect(detalle_post_save_receiver, sender=abono)

# post_delete.connect(detalle_post_save_receiver, sender=abono)
