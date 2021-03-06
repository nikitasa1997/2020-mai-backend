# Generated by Django 2.2.18 on 2021-02-08 09:46

from django.db import migrations, models
import django.db.models.expressions
import django.db.models.functions.datetime


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(db_column='full_name', max_length=255, verbose_name='Полное имя автора')),
                ('birth_date', models.DateField(db_column='birth_date', verbose_name='Дата рождения')),
                ('death_date', models.DateField(db_column='death_date', default='9999-12-31', verbose_name='Дата сметри')),
            ],
            options={
                'verbose_name': 'автор',
                'verbose_name_plural': 'авторы',
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', max_length=255, verbose_name='Заглавие книги')),
                ('pub_year', models.DateField(db_column='pub_year', verbose_name='Год публикации')),
                ('isbn', models.CharField(db_column='isbn', max_length=13, unique=True, verbose_name='Международный стандартный номер книги')),
                ('price', models.DecimalField(db_column='price', decimal_places=2, max_digits=19, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'книги',
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=255, unique=True, verbose_name='Название жанра')),
            ],
            options={
                'verbose_name': 'жанр',
                'verbose_name_plural': 'жанры',
                'db_table': 'genre',
            },
        ),
        migrations.AddConstraint(
            model_name='genre',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, name=''), name='genre_name_check'),
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='main.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='main.Genre'),
        ),
        migrations.AddConstraint(
            model_name='author',
            constraint=models.UniqueConstraint(fields=('full_name', 'birth_date'), name='author_full_name_birth_date_key'),
        ),
        migrations.AddConstraint(
            model_name='author',
            constraint=models.CheckConstraint(check=models.Q(full_name__regex='\\w{2,} (\\w{1,2}\\. |\\w{2,} )?\\w{2,}'), name='author_full_name_check'),
        ),
        migrations.AddConstraint(
            model_name='author',
            constraint=models.CheckConstraint(check=models.Q(birth_date__lt=django.db.models.expressions.F('death_date')), name='author_check'),
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.UniqueConstraint(fields=('title', 'pub_year'), name='book_title_pub_year_key'),
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, title=''), name='book_title_check'),
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.CheckConstraint(check=models.Q(('pub_year', django.db.models.functions.datetime.Trunc('pub_year', 'year', output_field=models.DateField())), ('pub_year__lt', django.db.models.functions.datetime.Now())), name='book_pub_year_check'),
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.CheckConstraint(check=models.Q(isbn__regex='\\d{13}'), name='book_isbn_check'),
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.CheckConstraint(check=models.Q(price__gt=0), name='book_price_check'),
        ),
    ]
