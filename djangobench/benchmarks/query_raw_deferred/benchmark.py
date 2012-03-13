from benchmark_harness import run_benchmark
from query_raw_deferred.models import MultiField
from djangobench.utils import do_syncdb


def benchmark():
    list(MultiField.objects.raw('select id from query_raw_deferred_multifield'))

def setup():
    do_syncdb(),
    for i in range(0, 1000):
        kwargs = {}
        for j in range(1, 11):
            kwargs['field%s' % j] = 'foobar_%s_%s' % (i, j)
        MultiField(**kwargs).save()

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A test for fetching large number of objects by Model.objects.all() with deferred fields.',
    }
)
