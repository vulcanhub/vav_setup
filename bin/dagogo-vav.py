###############################################################################
# Copyright (C) April 2022, Belmont Computing, Inc. -- All Rights Reserved
# Licensed under the BCI-SLA. See LICENSE for details.
#
# NOTICE:  All information contained herein is, and remains the property of
# Belmont Computing, Inc.  The intellectual and technical concepts contained
# herein are proprietary to Belmont Computing, Inc. and may be covered by U.S.
# and Foreign Patents, patents in process, and are protected by trade secret
# or copyright law.  Dissemination of this information or reproduction of this
# material is strictly forbidden unless prior written permission is obtained
# from Belmont Computing, Inc.
###############################################################################

import sys
import os

setup_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.join(setup_dir, 'libs'))

from dagogo_vav_core import main


if __name__ == '__main__':
    main()

