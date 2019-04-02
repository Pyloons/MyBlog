# Generated by Django 2.1.7 on 2019-03-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=144, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('status', models.CharField(choices=[('draft', '草稿'), ('publish', '公开')], default='draft', max_length=7, verbose_name='状态')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=144, verbose_name='名称')),
                ('path', models.CharField(max_length=200, verbose_name='路径')),
            ],
            options={
                'verbose_name': '文件',
                'verbose_name_plural': '文件',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=144, verbose_name='名称')),
                ('path', models.CharField(max_length=200, verbose_name='路径')),
            ],
            options={
                'verbose_name': '图片',
                'verbose_name_plural': '图片',
            },
        ),
    ]