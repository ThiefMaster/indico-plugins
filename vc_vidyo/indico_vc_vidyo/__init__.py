# This file is part of the Indico plugins.
# Copyright (C) 2002 - 2021 CERN
#
# The Indico plugins are free software; you can redistribute
# them and/or modify them under the terms of the MIT License;
# see the LICENSE file for more details.

from indico.core import signals
from indico.util.i18n import make_bound_gettext


_ = make_bound_gettext('vc_vidyo')


@signals.import_tasks.connect
def _import_tasks(sender, **kwargs):
    import indico_vc_vidyo.task  # noqa: F401
