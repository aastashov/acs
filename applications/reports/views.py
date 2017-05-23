# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from applications.reports.models import AccountingAccess


@login_required
def report_main(request, page_number=1):
    template = 'main_report.html'
    if 'header_search' in request.GET:
        accounting_list = AccountingAccess.objects.filter(user__first_name__contains=request.GET.get('username'))
    elif 'form_search' in request.GET:
        today = datetime.today()
        first_date = request.GET.get('first_date') or datetime.strftime(today, '%Y-%m-01')
        last_date = request.GET.get('last_date')
        last_date = today if not last_date else datetime.strptime(last_date, '%Y-%m-%d')
        last_date += timedelta(days=1)
        accounting_list = AccountingAccess.objects.filter(date__range=[first_date, last_date])
    else:
        accounting_list = AccountingAccess.objects.filter(date=datetime.today())
    paginator = Paginator(accounting_list.exclude(user__profile=None), 5)
    return render(request, template, {'user_list': paginator.page(page_number)})
