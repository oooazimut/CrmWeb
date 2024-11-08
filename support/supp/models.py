# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Employees(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.TextField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "employees"
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

    def __str__(self):
        return str(self.username)


class Entities(models.Model):
    ent_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "entities"
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"

    def __str__(self):
        return str(self.name)


class Tasks(models.Model):
    taskid = models.AutoField(primary_key=True)
    created = models.DateTimeField(verbose_name="Создано", blank=True, null=True)
    creator = models.IntegerField(verbose_name="Создал", blank=True, null=True)
    phone = models.IntegerField(verbose_name="Телефон", blank=True, null=True)
    title = models.TextField(verbose_name="Тема", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    media_type = models.TextField(blank=True, null=True)
    media_id = models.TextField(blank=True, null=True)
    status = models.TextField(verbose_name="Статус", blank=True, null=True)
    priority = models.TextField(verbose_name="Приоритет", blank=True, null=True)
    entity = models.ForeignKey(
        Entities, models.DO_NOTHING, db_column="entity", verbose_name='Объект', blank=True, null=True
    )
    slave = models.ForeignKey(
        Employees, models.DO_NOTHING, db_column="slave", verbose_name='Исполнитель', blank=True, null=True
    )
    result = models.TextField(blank=True, null=True)
    resulttype = models.TextField(blank=True, null=True)
    resultid = models.TextField(blank=True, null=True)
    act = models.IntegerField(blank=True, null=True)
    actid = models.TextField(blank=True, null=True)
    acttype = models.TextField(blank=True, null=True)
    agreement = models.TextField(verbose_name="Соглашение", blank=True, null=True)
    summary = models.TextField(
        verbose_name="Комментарий к закрытию", blank=True, null=True
    )

    class Meta:
        db_table = "tasks"
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
    def __str__(self):
        return str(self.created)+'   '+str(self.slave)+': '+str(self.title)+', '+str(self.status)
