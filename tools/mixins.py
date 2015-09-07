from django.contrib.auth.decorators import login_required, user_passes_test


class SuperuserRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(SuperuserRequiredMixin, cls).as_view(**initkwargs)
        return user_passes_test(lambda u: u.is_superuser)(view)