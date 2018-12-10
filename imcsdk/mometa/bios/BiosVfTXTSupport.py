"""This module contains the general information for BiosVfTXTSupport ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfTXTSupportConsts:
    VP_TXTSUPPORT_DISABLED = "Disabled"
    VP_TXTSUPPORT_ENABLED = "Enabled"
    _VP_TXTSUPPORT_DISABLED = "disabled"
    _VP_TXTSUPPORT_ENABLED = "enabled"
    VP_TXTSUPPORT_PLATFORM_DEFAULT = "platform-default"


class BiosVfTXTSupport(ManagedObject):
    """This is BiosVfTXTSupport class."""

    consts = BiosVfTXTSupportConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfTXTSupport", "biosVfTXTSupport", "TXT-Support", VersionMeta.Version304a, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfTXTSupport", "biosVfTXTSupport", "TXT-Support", VersionMeta.Version313h, "InputOutput", 0x1f, [], ["admin"], [u'biosPlatformDefaults', u'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_txt_support": MoPropertyMeta("vp_txt_support", "vpTXTSupport", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version313h, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version313h, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version313h, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_txt_support": MoPropertyMeta("vp_txt_support", "vpTXTSupport", "string", VersionMeta.Version313h, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpTXTSupport": "vp_txt_support", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpTXTSupport": "vp_txt_support", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_txt_support = None

        ManagedObject.__init__(self, "BiosVfTXTSupport", parent_mo_or_dn, **kwargs)

