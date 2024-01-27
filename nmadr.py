import qrcode

qr = qrcode.make('http://localhost:8000/admin/')
qr.save('admin.png')



# class Blog(CreatedBaseModel):
#     id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = CharField(max_length=255)
#     author = ForeignKey('apps.User', CASCADE)
#     category = ForeignKey('apps.Category', CASCADE)
#     image = ImageField(default='blog/default.jpg', upload_to='blog/images/')
#     tags = ManyToManyField('apps.Tag')
#     text = CKEditor5Field(blank=True, null=True, config_name='extends')
#
#     def count_comment(self):
#         return 2


# class BlogDetailView(DetailView):
#     queryset = Blog2.objects.order_by('-created_at')
#     template_name = 'apps/blogs/blog-details-left-sidebar.html'
#     pk_url_kwarg = 'pk'
#     context_object_name = 'blog'
#
#     def get_object(self, queryset=None):
#         return super().get_object(queryset)