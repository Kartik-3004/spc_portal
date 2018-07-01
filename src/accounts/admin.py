from django.contrib import admin
from company.models import JobOffer, InternshipOffer
from accounts.models import StudentProfile, CompanyPerson, CompanyProfile, Resume


class JobOfferInline(admin.StackedInline):
    model = JobOffer


class InternOfferInline(admin.StackedInline):
    model = InternshipOffer


class CompanyPersonInline(admin.StackedInline):
    model = CompanyPerson


class ResumeInline(admin.StackedInline):
    model = Resume


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    inlines = (ResumeInline,)

    class Meta:
        model = StudentProfile
        fields = '__all__'


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    inlines = (CompanyPersonInline, JobOfferInline, InternOfferInline)

    class Meta:
        model = CompanyProfile
        fields = '__all__'
