class DataMixin:
    def get_default_context(self, **kwargs):
        '''Возвращается контекст для передачи в шаблон'''
        context = kwargs
