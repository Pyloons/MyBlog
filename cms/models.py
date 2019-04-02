from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    STATUS_CHOICE = (
        ('draft','草稿'),
        ('publish','公开')
    )
    title = models.CharField('标题', max_length=144)
    content = RichTextUploadingField('内容')
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    status = models.CharField('状态', max_length=7, choices=STATUS_CHOICE, default='draft')
    is_top = models.BooleanField('是否置顶', default=False)
    cover_img = models.ImageField('封面图', upload_to='covers', null=True)

    class Meta:
        verbose_name = verbose_name_plural = '文章'

    def __str__(self):
        return self.title

    @classmethod
    def show_posts(self):
        return Article.objects.all()
    
    @classmethod
    def get_article_detail(self, article_id):
        try:
            article = Article.objects.get(id=article_id)
            if article.status != 'publish':
                return 'Not Found'
        except:
            return 'Not Found'
        return article

