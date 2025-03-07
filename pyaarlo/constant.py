DEFAULT_HOST = "https://myapi.arlo.com"

ORIGIN_HOST = "https://my.arlo.com"
REFERER_HOST = "https://my.arlo.com/"
MQTT_HOST = "mqtt-cluster.arloxcld.com"

DEVICES_PATH = "/hmsweb/v2/users/devices"
DEFINITIONS_PATH = "/hmsweb/users/automation/definitions"
AUTOMATION_PATH = "/hmsweb/users/devices/automation/active"
LIBRARY_PATH = "/hmsweb/users/library"
LOGIN_PATH = "/hmsweb/login/v2"
SESSION_PATH = "/hmsweb/users/session/v2"
LOGOUT_PATH = "/hmsweb/logout"
NOTIFY_PATH = "/hmsweb/users/devices/notify/"
SUBSCRIBE_PATH = "/hmsweb/client/subscribe"
UNSUBSCRIBE_PATH = "/hmsweb/client/unsubscribe"
MODES_PATH = "/hmsweb/users/devices/automation/active"
RECORD_START_PATH = "/hmsweb/users/devices/startRecord"
RECORD_STOP_PATH = "/hmsweb/users/devices/stopRecord"
RESTART_PATH = "/hmsweb/users/devices/restart"
STREAM_SNAPSHOT_PATH = "/hmsweb/users/devices/takeSnapshot"
STREAM_START_PATH = "/hmsweb/users/devices/startStream"
IDLE_SNAPSHOT_PATH = "/hmsweb/users/devices/fullFrameSnapshot"
CREATE_DEVICE_CERTS_PATH = "/hmsweb/users/devices/v2/security/cert/create"
RATLS_TOKEN_GENERATE_PATH = "/hmsweb/users/device/ratls/token"
RATLS_CONNECTIVITY_PATH = '/hmsls/connectivity'
RATLS_DOWNLOAD_PATH = "/hmsls/download"
RATLS_LIBRARY_PATH = "/hmsls/list"  # Supports list/{YYYYMMDD}/{YYYYMMMDD} or list/{YYYYMMDD}/{YYYYMMMDD}/{device_id}

MQTT_PATH = "/mqtt"
TRANSID_PREFIX = "web"

DEFAULT_AUTH_HOST = "https://ocapi-app.arlo.com"
AUTH_PATH = "/api/auth"
AUTH_START_PATH = "/api/startAuth"
AUTH_FINISH_PATH = "/api/finishAuth"
AUTH_GET_FACTORS = "/api/getFactors"
AUTH_VALIDATE_PATH = "/api/validateAccessToken"

TFA_CONSOLE_SOURCE = "console"
TFA_IMAP_SOURCE = "imap"
TFA_REST_API_SOURCE = "rest-api"
TFA_PUSH_SOURCE = "push"
TFA_EMAIL_TYPE = "EMAIL"
TFA_SMS_TYPE = "SMS"
TFA_PUSH_TYPE = "PUSH"
TFA_DELAY = 5
TFA_RETRIES = 5
TFA_DEFAULT_HOST = "https://pyaarlo-tfa.appspot.com"

PRELOAD_DAYS = 30

# Start up delays.
REFRESH_CAMERA_DELAY = 5
INITIAL_REFRESH_DELAY = REFRESH_CAMERA_DELAY + 3
MEDIA_LIBRARY_DELAY = 15
CAMERA_MEDIA_DELAY = MEDIA_LIBRARY_DELAY + 10

# Update intervals.
FAST_REFRESH_INTERVAL = 60
SLOW_REFRESH_INTERVAL = 10 * 60
EVENT_STREAM_TIMEOUT = (FAST_REFRESH_INTERVAL * 2) + 5
MODE_UPDATE_INTERVAL = 2

# update keys
ACTIVITY_STATE_KEY = "activityState"
AIR_QUALITY_KEY = "airQuality"
AUDIO_DETECTED_KEY = "audioDetected"
AUDIO_ANALYTICS_KEY = "audioAnalytics"
BATTERY_KEY = "batteryLevel"
BATTERY_TECH_KEY = "batteryTech"
BRIGHTNESS_KEY = "brightness"
BUTTON_PRESSED_KEY = "buttonPressed"
CHARGER_KEY = "chargerTech"
CHARGING_KEY = "chargingState"
CHIMES_KEY = "chimes"
CONNECTION_KEY = "connectionState"
CRY_DETECTION_KEY = "babyCryDetection"
FLIP_KEY = "flip"
HUMIDITY_KEY = "humidity"
LAMP_STATE_KEY = "lampState"
MIRROR_KEY = "mirror"
MOTION_DETECTED_KEY = "motionDetected"
MOTION_ENABLED_KEY = "motionSetupModeEnabled"
MOTION_SENS_KEY = "motionSetupModeSensitivity"
PING_CAPABILITY = "pingCapability"
POWER_SAVE_KEY = "powerSaveMode"
PRIVACY_KEY = "privacyActive"
LIGHT_BRIGHTNESS_KEY = "lightBrightness"
LIGHT_MODE_KEY = "lightMode"
RECORDING_STOPPED_KEY = "recordingStopped"
RESOURCE_CAPABILITY = "resourceCapability"
SILENT_MODE_KEY = "silentMode"
SPOTLIGHT_KEY = "spotlight"
SPOTLIGHT_BRIGHTNESS_KEY = "spotlightBrightness"
SIGNAL_STR_KEY = "signalStrength"
SIREN_STATE_KEY = "sirenState"
TEMPERATURE_KEY = "temperature"
TIMEZONE_KEY = "olsonTimeZone"
TRADITIONAL_CHIME_KEY = "traditionalChime"
NIGHTLIGHT_KEY = "nightLight"
MEDIA_PLAYER_KEY = "mediaPlayer"
FLOODLIGHT_KEY = "floodlight"
FLOODLIGHT_BRIGHTNESS1_KEY = "brightness1"
FLOODLIGHT_BRIGHTNESS2_KEY = "brightness2"

AUDIO_CONFIG_KEY = "config"
AUDIO_PLAYLIST_KEY = "playlist"
AUDIO_POSITION_KEY = "position"
AUDIO_SPEAKER_KEY = "speaker"
AUDIO_STATUS_KEY = "status"
AUDIO_TRACK_KEY = "trackId"

# we can get these from the resource; doorbell is subset
RESOURCE_KEYS = [
    ACTIVITY_STATE_KEY,
    AIR_QUALITY_KEY,
    AUDIO_DETECTED_KEY,
    BATTERY_KEY,
    BATTERY_TECH_KEY,
    BRIGHTNESS_KEY,
    CONNECTION_KEY,
    CHARGER_KEY,
    CHARGING_KEY,
    FLIP_KEY,
    HUMIDITY_KEY,
    LAMP_STATE_KEY,
    LIGHT_BRIGHTNESS_KEY,
    LIGHT_MODE_KEY,
    MIRROR_KEY,
    MOTION_DETECTED_KEY,
    MOTION_ENABLED_KEY,
    MOTION_SENS_KEY,
    POWER_SAVE_KEY,
    PRIVACY_KEY,
    SIGNAL_STR_KEY,
    SIREN_STATE_KEY,
    TEMPERATURE_KEY,
    AUDIO_CONFIG_KEY,
    AUDIO_PLAYLIST_KEY,
    AUDIO_STATUS_KEY,
    AUDIO_SPEAKER_KEY,
    AUDIO_TRACK_KEY,
    AUDIO_POSITION_KEY,
]

RESOURCE_UPDATE_KEYS = [
    ACTIVITY_STATE_KEY,
    AIR_QUALITY_KEY,
    AUDIO_CONFIG_KEY,
    AUDIO_DETECTED_KEY,
    AUDIO_PLAYLIST_KEY,
    AUDIO_POSITION_KEY,
    AUDIO_SPEAKER_KEY,
    AUDIO_STATUS_KEY,
    AUDIO_TRACK_KEY,
    BATTERY_KEY,
    BATTERY_TECH_KEY,
    CHARGER_KEY,
    CHARGING_KEY,
    CONNECTION_KEY,
    FLOODLIGHT_KEY,
    HUMIDITY_KEY,
    LAMP_STATE_KEY,
    MOTION_DETECTED_KEY,
    PRIVACY_KEY,
    SIGNAL_STR_KEY,
    SILENT_MODE_KEY,
    SIREN_STATE_KEY,
    TEMPERATURE_KEY,
]

RECENT_ACTIVITY_KEYS = [AUDIO_DETECTED_KEY, MOTION_DETECTED_KEY]

# device keys
CONNECTIVITY_KEY = "connectivity"
DEVICE_ID_KEY = "deviceId"
DEVICE_NAME_KEY = "deviceName"
DEVICE_TYPE_KEY = "deviceType"
MEDIA_COUNT_KEY = "mediaObjectCount"
PARENT_ID_KEY = "parentId"
UNIQUE_ID_KEY = "uniqueId"
USER_ID_KEY = "userId"
LAST_IMAGE_KEY = "presignedLastImageUrl"
LAST_RECORDING_KEY = "presignedLastRecordingUrl"
SNAPSHOT_KEY = "presignedFullFrameSnapshotUrl"
STREAM_SNAPSHOT_KEY = "presignedContentUrl"
XCLOUD_ID_KEY = "xCloudId"

LAST_VIDEO_CREATED_KEY = "lastCaptureVideoCreated"
LAST_VIDEO_URL_KEY = "lastCaptureVideoUrl"
LAST_VIDEO_THUMBNAIL_URL_KEY = "lastCaptureThumbnailUrl"
LAST_VIDEO_OBJECT_TYPE = "lastCaptureObjectType"
LAST_VIDEO_OBJECT_REGION = "lastCaptureObjectRegion"

DEVICE_KEYS = [
    ACTIVITY_STATE_KEY,
    DEVICE_ID_KEY,
    DEVICE_NAME_KEY,
    DEVICE_TYPE_KEY,
    LAST_IMAGE_KEY,
    MEDIA_COUNT_KEY,
    PARENT_ID_KEY,
    SNAPSHOT_KEY,
    UNIQUE_ID_KEY,
    USER_ID_KEY,
    XCLOUD_ID_KEY,
]

MEDIA_UPLOAD_KEYS = [MEDIA_COUNT_KEY, LAST_IMAGE_KEY]

# custom keys
CAPTURED_TODAY_KEY = "capturedToday"
LAST_CAPTURE_KEY = "lastCapture"
MODE_KEY = "activeMode"
MODES_KEY = "configuredMode"
LAST_IMAGE_DATA_KEY = "presignedLastImageData"
LAST_IMAGE_SRC_KEY = "lastImageSource"
MEDIA_UPLOAD_KEY = "mediaUploadNotification"
MODE_NAME_TO_ID_KEY = "modeNameToId"
MODE_ID_TO_NAME_KEY = "modeIdToName"
MODE_IS_SCHEDULE_KEY = "modeIsSchedule"
RECENT_ACTIVITY_KEY = "recentActivity"
SCHEDULE_KEY = "activeSchedule"
TOTAL_BELLS_KEY = "totalDoorBells"
TOTAL_CAMERAS_KEY = "totalCameras"
TOTAL_LIGHTS_KEY = "totalLights"
SILENT_MODE_CALL_KEY = "call"
SILENT_MODE_ACTIVE_KEY = "active"

# Media player
MEDIA_PLAYER_RESOURCE_ID = "audioPlayback/player"
DEFAULT_TRACK_ID = "229dca67-7e3c-4a5f-8f43-90e1a9bffc38"

BLANK_IMAGE = (
    "iVBORw0KGgoAAAANSUhEUgAAAKAAAABaCAQAAACVz5XZAAAAh0lEQVR42u3QMQ0AAAgDMOZf9BDB"
    "RdJKaNrhIAIFChQoEIECBQpEoECBAhEoUKBABAoUKBCBAgUKRKBAgQIRKFCgQAQKFCgQgQIFCkSg"
    "QIECBSJQoECBCBQoUCACBQoUiECBAgUiUKBAgQgUKFAgAgUKFIhAgQIFIlCgQIEIFChQoECBAgV+"
    "tivOs6f/QsrFAAAAAElFTkSuQmCC"
)

VIDEO_CONTENT_TYPES = ['2k', '4k', 'hd']

# DEFAULT_MODES = [ { u'id':u'mode0',u'type':u'disarmed' }, { u'id':u'mode1',u'type':u'armed' } ]
DEFAULT_MODES = {"disarmed": "mode0", "armed": "mode1"}
DEFAULT_RESOURCES = {"modes", "siren", "doorbells", "lights", "cameras", "devices"}

# MODEL PREFIXES
MODEL_HD = "VMC3030"
MODEL_PRO_2 = "VMC4030"
MODEL_PRO_3 = "VMC4040"
MODEL_PRO_4 = "VMC4041"
MODEL_PRO_3_FLOODLIGHT = "FB1001"
MODEL_ULTRA = "VMC5040"
MODEL_BABY = "ABC1000"
MODEL_ESSENTIAL = "VMC2030"
MODEL_ESSENTIAL_INDOOR = "VMC2040"

MODEL_WIRED_VIDEO_DOORBELL = "AVD1001"
MODEL_WIREFREE_VIDEO_DOORBELL = "AVD2001"

MODEL_GO = "VML4030"

USER_AGENTS = {
    "arlo":
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) "
        "AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 NETGEAR/v1 "
        "(iOS Vuezone)",
    "iphone":
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_3 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1",
    "ipad":
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1",
    "mac":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15",
    "firefox":
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) "
        "Gecko/20100101 Firefox/85.0",
    "linux":
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
}

CERT_BEGIN = '-----BEGIN CERTIFICATE-----\n'
CERT_END = '-----END CERTIFICATE-----\n'
