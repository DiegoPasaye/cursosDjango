from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Curso(models.Model):
    nombre = models.CharField(
        max_length=100,
        verbose_name='Nombre del Curso',
        help_text="Introduce el nombre completo del curso."
    )
    descripcion = models.TextField(
        verbose_name='Descripción Detallada',
        help_text="Proporciona una descripción completa del contenido del curso."
    )
    imagen = models.ImageField(
        upload_to='cursos_imagenes/',
        null=True,
        blank=True,
        verbose_name='Imagen del Curso',
        help_text="Sube una imagen representativa del curso."
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de Creación',
        help_text="Fecha y hora en que se registró el curso. Se genera automáticamente."
    )
    duracion_horas = models.PositiveIntegerField(
        verbose_name='Duración (horas)',
        help_text="Número de horas que dura el curso.",
        default=0
    )
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Precio ($)',
        help_text="Costo del curso en pesos."
    )
    activo = models.BooleanField(
        default=True,
        verbose_name='Activo',
        help_text="Marca si el curso está actualmente disponible."
    )
    cupo_maximo = models.SmallIntegerField(
        verbose_name='Cupo Máximo',
        help_text="Número máximo de estudiantes permitidos en el curso.",
        null=True, blank=True
    )
    CATEGORIAS = [
        ('PROG', 'Programación'),
        ('BD', 'Bases de Datos'),
        ('DIS', 'Diseño'),
        ('MARK', 'Marketing'),
        ('OTRO', 'Otro'),
    ]
    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIAS,
        default='PROG',
        verbose_name='Categoría',
        help_text="Selecciona la categoría a la que pertenece el curso."
    )

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['fecha_creacion']

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    id_actividad = models.AutoField(primary_key=True, verbose_name="Clave de Actividad")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso Relacionado")
    nombre_actividad = models.CharField(max_length=150, verbose_name="Nombre de la Actividad")
    descripcion_Actividad = RichTextField(verbose_name="Comentario")
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de Creación',
        help_text="Fecha y hora en que se registró el curso. Se genera automáticamente."
    )

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = ['fecha_creacion']

    def __str__(self):
        return self.nombre_actividad