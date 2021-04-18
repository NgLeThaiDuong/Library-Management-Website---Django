from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta

class Book (models.Model):
    class Subject(models.IntegerChoices):
        GENERALITIES          = 0, _("Generalities")
        PHILOSOPHY_PSYCHOLOGY = 1, _("Philosophy & psychology")
        RELIGION              = 2, _("Religion")
        SOCIALSCIENCE         = 3, _("Social sciences")
        LANGUAGES             = 4, _("Languages")
        NATURESCIENCE_MATHEMATICS = 5, _("Natural sciences & mathematics")
        TECHNOLOGY            = 6, _("Technology")
        THEARTS               = 7, _("The arts")
        LITERATURE_RHETORIC   = 8, _("Literature & rhetoric")
        GEOGRAPHY_HISTORY     = 9, _(" Geography & history")

    title = models.CharField("Tiêu đề", max_length=255)
    author = models.CharField("Tác giả",max_length=255)
    subject = models.IntegerField("Chu de", choices = Subject.choices, default=None)
    publisher = models.CharField("Nhà xuất bản",max_length=255)
    pubdate = models.IntegerField("Năm xuất bản")
    size = models.CharField("Kích thước", max_length=7)
    pages = models.IntegerField("Số trang")
    entry_date = models.DateField("Ngày nhập", auto_now_add=True)
    book_cover = models.ImageField("Bìa sách", upload_to='book_cover', null=True, blank=True, default="book_cover/default_book_cover.jpg")
    status = models.BooleanField("Sẵn có", default=True)
    
    def __str__ (self):
        display = str(self.id) + " - " + self.title 
        return display

    def subject_verbose(self):
        return dict(Book.Subject)[self.subject]
    
class Librarian (models.Model):
    name = models.CharField("Tên nhân viên", max_length=255)
    date_of_birth = models.DateField("Ngày sinh nhân viên")
    tel_number = models.CharField("Số điện thoại nhân viên", max_length=255)
    email = models.CharField("Địa chỉ email", max_length=254, unique=True)

    
    def __str__ (self):
        display = str(self.id) + " - " + self.name
        return display 

class Member (models.Model):
    name = models.CharField("Họ và Tên", max_length=255)
    date_of_birth = models.DateField("Ngày sinh")
    tel_number = models.CharField("Số điện thoại", max_length=255, unique=True)
    resgister_date = models.DateField("Ngày đăng ký", auto_now_add=True)
    email = models.CharField("Email", default=None, blank=False, max_length=255, unique=True)
    avatar = models.ImageField("Ảnh đại diện", upload_to='user_avatar', null=True, blank=True, default='user_avatar/default_avatar.png')

    def __str__ (self):
        display = str(self.id) + " - " +self.name
        return display 

class LibraryCard(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE,verbose_name="Mã thành viên")
    active_date = models.DateField("Ngày kích hoạt", auto_now_add=True)
    deactive_date = models.DateField("Ngày vô hiệu hóa", null=True)

class BookRequest (models.Model):
    member = models.ForeignKey(Member, on_delete = models.CASCADE, verbose_name="Mã thành viên yêu cầu")
    requested_date = models.DateField("Ngày yêu cầu",auto_now_add=True)
    requested_book_title = models.CharField("Tên sách yêu cầu",max_length=255)
    requested_book_author = models.CharField("Tác giả sách yêu cầu",max_length=255)
    status = models.BooleanField("Trạng thái xử lý", default=False)

class BookLending (models.Model):
    member = models.ForeignKey(Member, on_delete=models.RESTRICT, verbose_name="Mã thành viên mượn")
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, verbose_name="Mã sách được mượn",)
    creation_date = models.DateField("Ngày mượn",auto_now_add=True)
    return_date = models.DateField("Ngày trả", null=True)

    def due_date(self):
        due_date = self.creation_date + timedelta(days=14)
        return due_date

    class Meta:
        ordering = ['-creation_date']

class BookLendingForm(ModelForm):
    class Meta:
        model = BookLending
        fields = ['member', 'book']
    def __init__(self, *args, **kwargs):
        super(BookLendingForm, self).__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.filter(status=True)


class BookReturnForm(ModelForm):
    class Meta:
        model = BookLending
        fields = ['member', 'book']
    def __init__(self, *args, **kwargs):
        super(BookReturnForm, self).__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.filter(status=False)