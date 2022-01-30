from django.db import models
from django.urls import reverse


class Manufacturer(models.Model):
    company = models.CharField(max_length=20, unique=True, verbose_name='Производитель')

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.company


PROC_CHOICES = [
    ('GOOGLE TENSOR', 'Google Tensor'),
    ('SNAPDRAGON 8 GEN 1', 'Snapdragon 8 Gen 1'),
    ('SNAPDRAGON 888', 'Snapdragon 888'),
    ('SNAPDRAGON 870', 'Snapdragon 870'),
    ('SNAPDRAGON 865', 'Snapdragon 865'),
    ('SNAPDRAGON 860', 'Snapdragon 860'),
    ('DIMENSITY 1200', 'Dimensity 1200'),
    ('DIMENSITY 1100', 'Dimensity 1100'),
    ('HELIO G96', 'Helio G96'),
    ('HELIO G95', 'Helio G95'),
    ('HELIO G90T', 'Helio G90T'),
    ('HELIO G88', 'Helio G88'),
    ('HELIO G85', 'Helio G85'),
    ('HELIO G80', 'Helio G80'),
    ('KIRIN 9000E', 'Kirin 9000E'),
    ('EXYNOS 1080', 'Exynos 1080'),
    ('EXYNOS 990', 'Exynos 990'),
    ('A15', 'A15 Bionic'),
    ('A14', 'A14 Bionic'),
    ('A13', 'A13 Bionic'),
    ('A12', 'A12 Bionic'),
    ('A11', 'A11 Bionic'),
    ('EXYNOS 2200', 'Exynos 2200'),
    ('EXYNOS 2100', 'Exynos 2100'),
]

RAM_CHOICES = [
    ('1GB', '1Gb'),
    ('2GB', '2Gb'),
    ('3GB', '3Gb'),
    ('4GB', '4Gb'),
    ('6GB', '6Gb'),
    ('8GB', '8Gb'),
    ('12GB', '12Gb'),
    ('16GB', '16GB'),
]

ROM_CHOICES = [
    ('8GB', '8Gb'),
    ('16GB', '16Gb'),
    ('32GB', '32Gb'),
    ('64GB', '64Gb'),
    ('128GB', '128Gb'),
    ('256GB', '256Gb'),
    ('512GB', '512Gb'),
    ('1024GB', '1024Gb'),
]

TYPE_DISPLAY_CHOICES = [
    ('IPS', 'IPS'),
    ('IPS+', 'IPS+'),
    ('LCD', 'LCD'),
    ('LTPS', 'LTPS'),
    ('OLED', 'OLED'),
    ('PLS', 'PLS'),
    ('AMOLED', 'AMOLED'),
    ('DYNAMIC AMOLED', 'Dynamic AMOLED'),
    ('DYNAMIC AMOLED 2X', 'Dynamic AMOLED 2X'),

]

COLOR_CHOICES = [
    ('BLACK', 'Черный'),
    ('RED', 'Красный'),
    ('WHITE', 'Белый'),
    ('PINK', 'Розовый'),
    ('BEIGE', 'Бежевый'),
    ('TURQUOISE', 'Бирюзовый'),
    ('BLUE', 'Голубой'),
    ('YELLOW', 'Желтый'),
    ('GREEN', 'Зелёный'),
    ('RED', 'Красный'),
    ('ORANGE', 'Оранжевый'),
    ('GREY', 'Серый'),
    ('DARK BLUE', 'Синий'),
    ('VIOLET', 'Фиолетовый'),
]

MP_CHOICES = [
    ('2MP', '2Mp'),
    ('5MP', '5Mp'),
    ('8MP', '8Mp'),
    ('10MP', '10Mp'),
    ('12MP', '12Mp'),
    ('13MP', '13Mp'),
    ('16MP', '16Mp'),
    ('21MP', '21Mp'),
    ('48MP', '48Mp'),
    ('50MP', '50Mp'),
    ('64MP', '64Mp'),
    ('108MP', '108Mp'),
]


class Phone(models.Model):
    model = models.CharField(max_length=30, verbose_name='Модель')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, verbose_name='Производитель')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    proc = models.CharField(max_length=40, choices=PROC_CHOICES, default='SNAPDRAGON 870', verbose_name='Процессор')
    ram = models.CharField(max_length=4, choices=RAM_CHOICES, default='4GB', verbose_name='Оперативная память')
    rom = models.CharField(max_length=6, choices=ROM_CHOICES, default='16GB', verbose_name='Накопитель')
    type_display = models.CharField(max_length=17, choices=TYPE_DISPLAY_CHOICES, default='IPS', verbose_name='Дисплей')
    diag_display = models.CharField(max_length=5, default='5', verbose_name='Диагональ')
    main_camera = models.CharField(max_length=6, choices=MP_CHOICES, default='2MP', verbose_name='Основная камера')
    front_camera = models.CharField(max_length=6, choices=MP_CHOICES, default='2MP', verbose_name='Фронтальная камера')
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='BLACK', verbose_name='Цвет')
    count = models.PositiveIntegerField(default=0, verbose_name='Количество')
    battery = models.PositiveIntegerField(default='4000', verbose_name='Емкость аккумулятора')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    year = models.PositiveIntegerField(default=2000, verbose_name='Год выпуска')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    def get_absolute_url(self):
        return reverse('phone_detail', args=[str(self.slug)])

    def __str__(self):
        return self.model
