class VTSInternalServerError(Exception):
    """VTube Studio error 'InternalServerError'."""

class VTSAPIAccessDeactivated(Exception):
    """VTube Studio error 'APIAccessDeactivated'."""

class VTSJSONInvalid(Exception):
    """VTube Studio error 'JSONInvalid'."""

class VTSAPINameInvalid(Exception):
    """VTube Studio error 'APINameInvalid'."""

class VTSAPIVersionInvalid(Exception):
    """VTube Studio error 'APIVersionInvalid'."""

class VTSRequestIDInvalid(Exception):
    """VTube Studio error 'RequestIDInvalid'."""

class VTSRequestTypeUnknown(Exception):
    """VTube Studio error 'RequestTypeUnknown'."""

class VTSRequestTypeMissingOrEmpty(Exception):
    """VTube Studio error 'RequestTypeMissingOrEmpty'."""

class VTSRequestRequiresAuthetication (Exception):
    """VTube Studio error 'RequestRequiresAuthetication '."""

class VTSTokenRequestDenied(Exception):
    """VTube Studio error 'TokenRequestDenied'."""

class VTSTokenRequestCurrentlyOngoing(Exception):
    """VTube Studio error 'TokenRequestCurrentlyOngoing'."""

class VTSTokenRequestPluginNameInvalid(Exception):
    """VTube Studio error 'TokenRequestPluginNameInvalid'."""

class VTSTokenRequestDeveloperNameInvalid(Exception):
    """VTube Studio error 'TokenRequestDeveloperNameInvalid'."""

class VTSTokenRequestPluginIconInvalid(Exception):
    """VTube Studio error 'TokenRequestPluginIconInvalid'."""

class VTSAuthenticationTokenMissing(Exception):
    """VTube Studio error 'AuthenticationTokenMissing'."""

class VTSAuthenticationPluginNameMissing(Exception):
    """VTube Studio error 'AuthenticationPluginNameMissing'."""

class VTSAuthenticationPluginDeveloperMissing(Exception):
    """VTube Studio error 'AuthenticationPluginDeveloperMissing'."""

class VTSModelIDMissing(Exception):
    """VTube Studio error 'ModelIDMissing'."""

class VTSModelIDInvalid(Exception):
    """VTube Studio error 'ModelIDInvalid'."""

class VTSModelIDNotFound(Exception):
    """VTube Studio error 'ModelIDNotFound'."""

class VTSModelLoadCooldownNotOver(Exception):
    """VTube Studio error 'ModelLoadCooldownNotOver'."""

class VTSCannotCurrentlyChangeModel(Exception):
    """VTube Studio error 'CannotCurrentlyChangeModel'."""

class VTSHotkeyQueueFull(Exception):
    """VTube Studio error 'HotkeyQueueFull'."""

class VTSHotkeyExecutionFailedBecauseNoModelLoaded(Exception):
    """VTube Studio error 'HotkeyExecutionFailedBecauseNoModelLoaded'."""

class VTSHotkeyIDNotFoundInModel(Exception):
    """VTube Studio error 'HotkeyIDNotFoundInModel'."""

class VTSHotkeyCooldownNotOver(Exception):
    """VTube Studio error 'HotkeyCooldownNotOver'."""

class VTSHotkeyIDFoundButHotkeyDataInvalid(Exception):
    """VTube Studio error 'HotkeyIDFoundButHotkeyDataInvalid'."""

class VTSHotkeyExecutionFailedBecauseBadState(Exception):
    """VTube Studio error 'HotkeyExecutionFailedBecauseBadState'."""

class VTSHotkeyUnknownExecutionFailure(Exception):
    """VTube Studio error 'HotkeyUnknownExecutionFailure'."""

class VTSColorTintRequestNoModelLoaded(Exception):
    """VTube Studio error 'ColorTintRequestNoModelLoaded'."""

class VTSColorTintRequestMatchOrColorMissing(Exception):
    """VTube Studio error 'ColorTintRequestMatchOrColorMissing'."""

class VTSColorTintRequestInvalidColorValue(Exception):
    """VTube Studio error 'ColorTintRequestInvalidColorValue'."""

class VTSMoveModelRequestNoModelLoaded(Exception):
    """VTube Studio error 'MoveModelRequestNoModelLoaded'."""

class VTSMoveModelRequestMissingFields(Exception):
    """VTube Studio error 'MoveModelRequestMissingFields'."""

class VTSMoveModelRequestValuesOutOfRange(Exception):
    """VTube Studio error 'MoveModelRequestValuesOutOfRange'."""
