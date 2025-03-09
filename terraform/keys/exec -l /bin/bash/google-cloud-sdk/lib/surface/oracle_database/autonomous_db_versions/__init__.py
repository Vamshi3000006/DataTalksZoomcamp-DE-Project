# -*- coding: utf-8 -*- #
# Copyright 2024 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This file is autogenerated and should not be edited by hand.
# AUTOGEN_CLI_VERSION: HEAD
"""Manage Autonomous Db Version resources."""

from googlecloudsdk.calliope import base
from surface.oracle_database.autonomous_db_versions import _init_extensions as extensions


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
@base.Autogenerated
@base.Hidden
class AutonomousDbVersionsAlpha(extensions.AutonomousDbVersionsAlpha):
  """Manage Autonomous Db Version resources."""


@base.ReleaseTracks(base.ReleaseTrack.GA)
@base.Autogenerated
class AutonomousDbVersionsGa(extensions.AutonomousDbVersionsGa):
  """Manage Autonomous Db Version resources."""
