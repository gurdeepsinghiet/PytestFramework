/*******************************************************************/
/*                                                                 */
/*               Copyright (C) 2021 Thales Group                   */
/*                      All Rights Reserved.                       */
/*                                                                 */
/*     This Module contains Proprietary Information of Thales      */
/*          Group, and should be treated as Confidential.          */
/*******************************************************************/

/**
 * \mainpage Sentinel Licensing API
 * \file licensing.h Sentinel Licensing API declarations
 */




#ifndef SNTL_LICENSING_H
#define SNTL_LICENSING_H

/* H****************************************************************
* FILENAME    : licensing.h
*
* DESCRIPTION :
*           Contains public function prototypes, macros and defines
*           needed for licensing an application using Sentinel Developer Kit.
* USAGE       :
*           This file should be included by all users of Sentinel Developer Kit.
*
*H*/

#ifdef __cplusplus
extern "C" {
#endif

#define SNTL_COPYRIGHT_STR    "  Copyright (C) 2021 Thales Group\n       All Rights Reserved.\n\n"

/**
* @defgroup Macros, typedefs Sentinel Types and Status Codes
* @{
*/

#define SNTL_DECLARE(_type)                _type

/*! Max Feature Name Length. */
#define SNTL_MAX_FEATURE_NAME_LEN          25 

/*! Max Feature Version Length. */
#define SNTL_MAX_FEATURE_VERSION_LEN       12  

/*! Max Contact Server Name Length. */
#define SNTL_MAX_SERVER_NAME_LEN           64 

/*! Max Vendor Usage Data Length. */
#define SNTL_MAX_VENDOR_USAGE_DATA_LEN     255

/*! Max Challenge Data Length. */
#define SNTL_MAX_CHAL_DATA_LEN             30 

/*! Max Response Data Length. */
#define SNTL_MAX_RESP_DATA_LEN             16 

/*! Max Vendor Identifier Length. */
#define SNTL_MAX_VENDOR_IDENTIFIER_LEN     25  

/*! Max Custom Host Name Length. */
#define SNTL_MAX_CUSTOM_HOSTNAME_LEN       31 

/*! Max Identity User Name Length. */
#define SNTL_MAX_IDENTITY_USERNAME_LEN     31

/*! Max File Path Length. */
#define SNTL_MAX_FILE_PATH_LEN             256


/*! Sentinel Status Codes */
enum sntl_status_codes
{
/*! The function executed successfully. */
   SNTL_SUCCESS = 0,

/*! Generic error when a license is denied by a server.
*   If reasons are known, more specific errors are given. */
   SNTL_NO_LICENSE_GIVEN = 210001,

/*! Application has not been given a name. */
   SNTL_APP_UNNAMED = 210002,

/*! Failed to resolve the server host. */
   SNTL_HOST_UNKNOWN = 210003,

/*! Failed to figure out the license server correctly. Set environment
*   variable LSHOST to (tilde-separated) name(s) of server(s). */
   SNTL_NO_SERVER_FILE = 210004,

/*! License server is not RUNNING. */
   SNTL_NO_SERVER_RUNNING = 210005,

/*! Feature is not licensed to run on this machine due to server/client
*   lock-code mismatch.  */
   SNTL_APP_NODE_LOCKED = 210006,

/*! DEPRECATED - Please use SNTL_LOGIN_SESSION_NOT_FOUND */
/*! Attempt to return a non-existent token by the client application. */
   SNTL_NO_KEY_TO_RETURN = 210007,

/*! Attempt to return a non-existent token by the client application. */
   SNTL_LOGIN_SESSION_NOT_FOUND = 210007,

/*! Failed to return the token issued to this client application. */
   SNTL_RETURN_FAILED = 210008,

/*! No more clients exist for this feature. */
   SNTL_NO_MORE_CLIENTS = 210009,

/*! No more features available on license server. */
   SNTL_NO_MORE_FEATURES = 210010,

/*! Error in calling API. */
   SNTL_CALLING_ERROR = 210011,

/*! Internal error in licensing or accessing feature. */
   SNTL_INTERNAL_ERROR = 210012,

/*! Irrecoverable Internal error in licensing or accessing feature. */
   SNTL_SEVERE_INTERNAL_ERROR = 210013,

/*! On the specified machine, license server is not responding.
 *  (Probable cause - network down, wrong port number, some other
 *  application on that port, etc.). */
   SNTL_NO_SERVER_RESPONSE = 210014,

/*! This user/machine has been excluded from accessing the feature. */
   SNTL_USER_EXCLUDED = 210015,

/*! Unknown shared id. */
   SNTL_UNKNOWN_SHARED_ID = 210016,

/*! No server responded to client broadcast. */
   SNTL_NO_RESPONSE_TO_BROADCAST = 210017,

/*! No such feature is available on the license server. */
   SNTL_NO_SUCH_FEATURE = 210018,

/*! Failed to add license. */
   SNTL_ADD_LIC_FAILED = 210019,

/*! Failed to delete license. */
   SNTL_DELETE_LIC_FAILED = 210020,

/*! Last update was done locally. */
   SNTL_LOCAL_UPDATE = 210021,

/*! Last update was done by the license server. */
   SNTL_REMOTE_UPDATE = 210022,

/*! 1. The vendor identification of requesting application does not match
*      with that of the application licensed by this system.
*   2. License of different vendor is being added to an isolated server. */
   SNTL_VENDORIDMISMATCH = 210023,

/*! Feature is licensed by multiple vendors other than your vendor. */
   SNTL_MULTIPLE_VENDORID_FOUND = 210024,

/*! An error has occurred in decrypting (or decoding) a network message. */
   SNTL_BAD_SERVER_MESSAGE = 210025,

/*! Operation is denied due to clock tamper detection. */
   SNTL_CLK_TAMP_FOUND = 210026,

/*! The specified operation is not permitted - authorization failed. */
   SNTL_NOT_AUTHORIZED = 210027,

/*! The domain of server is different from that of client. */
   SNTL_INVALID_DOMAIN = 210028,

/*! The specified log filename not found on license server. */
   SNTL_LOG_FILE_NAME_NOT_FOUND = 210034,

/*! Cannot change specified log filename on license server. */
   SNTL_LOG_FILE_NAME_NOT_CHANGED = 210035,

/*! Machine's fingerprint mismatch for feature. */
   SNTL_FINGERPRINT_MISMATCH = 210036,

/*! Trial license usage exhausted or trial days expired. */
   SNTL_TRIAL_LIC_EXHAUSTED = 210037,

/*! No updates have taken place so far. */
   SNTL_NO_UPDATES_SO_FAR = 210038,

/*! Returned all the tokens for this feature. */
   SNTL_ALL_UNITS_RELEASED = 210039,

/*! The LS_HANDLE is a queued handle. */
   SNTL_QUEUED_HANDLE = 210040,

/*! The LS_HANDLE is an active handle. */
   SNTL_ACTIVE_HANDLE = 210041,

/*! The status of client handle is ambiguous. */
   SNTL_AMBIGUOUS_HANDLE = 210042,

/*! Could not queue the client because the queue is full. */
   SNTL_NOMORE_QUEUE_RESOURCES = 210043,

/*! No client as specified, found with the server. */
   SNTL_NO_SUCH_CLIENT = 210044,

/*! Client not authorized to make the specified request. */
   SNTL_CLIENT_NOT_AUTHORIZED = 210045,

/*! Processing not done because current leader is not known. */
   SNTL_LEADER_NOT_PRESENT = 210047,

/*! Tried to add a server to pool which is already there. */
   SNTL_SERVER_ALREADY_PRESENT = 210048,

/*! Tried to delete a server which is not in pool currently. */
   SNTL_SERVER_NOT_PRESENT = 210049,

/*! File can not be opened. */
   SNTL_FILE_OPEN_ERROR = 210050,

/*! Host name is either not valid or can not be resolved. */
   SNTL_BAD_HOSTNAME = 210051,

/*! The License Manager fails to identify the client library version. */
   SNTL_DIFF_LIB_VER = 210052,

/*! A non-redundant server contacted for redundant server related information. */
   SNTL_NON_REDUNDANT_SRVR = 210053,

/*! Message forwarded to leader license server. */
   SNTL_MSG_TO_LEADER = 210054,

/*! Update failure. May be server died or modified. */
   SNTL_CONTACT_FAILOVER_SERVER = 210055,

/*! IP address given can not be resolved. */
   SNTL_UNRESOLVED_IP_ADDRESS = 210056,

/*! Hostname given is can not be resolved. */
   SNTL_UNRESOLVED_HOSTNAME = 210057,

/*! Invalid IP address format. */
   SNTL_INVALID_IP_ADDRESS = 210058,

/*! Server is synchronizing dist table. */
   SNTL_SERVER_FILE_SYNC = 210059,

/*! Pool is already having maximum number of servers it can handle. */
   SNTL_POOL_FULL = 210060,

/*! Pool will not exist if this only server is removed. */
   SNTL_ONLY_SERVER = 210061,

/*! The feature is inactive on the requested server. */
   SNTL_FEATURE_INACTIVE = 210062,

/*! The token cannot be issued because of majority rule failure. */
   SNTL_MAJORITY_RULE_FAILURE = 210063,

/*! Configuration file modifications failed. */
   SNTL_CONF_FILE_ERROR = 210064,

/*! A non-redundant feature contacted for redundant feature related operation. */
   SNTL_NON_REDUNDANT_FEATURE = 210065,

/*! Can not find trial usage information for given feature. */
   SNTL_NO_TRIAL_INFO = 210066,

/*! Failure in retrieving the trial usage information for the given feature. */
   SNTL_TRIAL_INFO_FAILED = 210067,

/*! Application is not linked to integrated library. */
   SNTL_NOT_LINKED_TO_INTEGRATED_LIBRARY = 210069,

/*! Client commuter code does not exist. */
   SNTL_CLIENT_COMMUTER_CODE_DOES_NOT_EXIST = 210070,

/*! No more checked-out commuter code exists on the client. */
   SNTL_NO_MORE_COMMUTER_CODE = 210072,

/*! Failed to get client commuter information. */
   SNTL_GET_COMMUTER_INFO_FAILED = 210073,

/*! Unable to uninstall the client commuter license. */
   SNTL_UNABLE_TO_UNINSTALL_CLIENT_COMMUTER_CODE = 210074,

/*! Unable to issue a commuter license to client. */
   SNTL_ISSUE_COMMUTER_CODE_FAILED = 210075,

/*! A non-commuter license is requested for commuter related operation. */
   SNTL_UNABLE_TO_ISSUE_COMM_CODE_OR_NON_COMM_LICENSE = 210076,

/*! DEPRECATED - Please use SNTL_COMMUTER_INSUFFICIENTUNITS */
/*! Not enough keys are available to check out commuter code. */
   SNTL_NOT_ENOUGH_COMMUTER_KEYS_AVAILABLE = 210077,
   
/*! Not enough tokens are available to check out commuter code. */
   SNTL_COMMUTER_INSUFFICIENTUNITS = 210077,

/*! Invalid commuter information from client. */
   SNTL_INVALID_INFO_FROM_CLIENT = 210078,

/*! Server has already checked out one commuter code for this client. */
   SNTL_CLIENT_ALREADY_EXIST = 210079,

/*! Client has already had commuter code with this feature version. */
   SNTL_COMMUTER_CODE_ALREADY_EXIST = 210081,

/*! Redundant server synchronization in progress, not an error. */
   SNTL_SERVER_SYNC_IN_PROGRESS = 210082,

/*! This commuter license is checked out remotely, so it cannot be checked-in. */
   SNTL_REMOTE_CHECKOUT = 210083,

/*! Unable to install commuter code. */
   SNTL_UNABLE_TO_INSTALL_COMMUTER_CODE = 210084,

/*! Failed to get locking code string. */
   SNTL_UNABLE_TO_GET_MACHINE_ID_STRING = 210085,

/*! Invalid locking code string. */
   SNTL_INVALID_MACHINEID_STR = 210086,

/*! Commuter code expiration is greater than license itself. */
   SNTL_EXCEEDS_LICENSE_LIFE = 210087,

/*! Operating in stand-alone mode using terminal client, not allowed by vendor. */
   SNTL_TERMINAL_SERVER_FOUND = 210088,

/*! DEPRECATED - Please use SNTL_NOT_SUPPORTED_IN_NET_ONLY_MODE or SNTL_NOT_SUPPORTED_IN_NET_LIBRARY_OR_MODE. */
/*! The feature is not supported in the Net-Only mode of library. */
    SNTL_INAPPROPRIATE_LIBRARY = 210089,

/*! The feature is not supported in the Net-Only mode of library. */
   SNTL_NOT_SUPPORTED_IN_NET_ONLY_MODE = 210089,

/*! The feature is not supported in the Net-Only lib/mode of server. */
   SNTL_NOT_SUPPORTED_IN_NET_LIBRARY_OR_MODE = 210089,

/*! The specified file type is not supported. */
   SNTL_INVALID_FILETYPE = 210090,

/*! The requested operation is not supported on this license server. */
   SNTL_NOT_SUPPORTED = 210091,

/*! License string is invalid. */
   SNTL_INVALID_LICENSE = 210092,

/*! License string is duplicate and already available on the server. */
   SNTL_DUPLICATE_LICENSE = 210093,

/*! Deletion of upgraded feature/license is not allowed. */
   SNTL_CANNOT_DELETE_UPGRADED_LIC = 210097,

/*! License upgrade feature is not allowed for redundant licenses, commuter
*   licenses and trial licenses. */
   SNTL_UPGRADE_NOT_ALLOWED = 210098,

/*! This feature is already marked for check-in. */
   SNTL_FEATURE_MARKED_FOR_DELETION = 210099,

/*! A network server is contacted for standalone related information. */
   SNTL_NETWORK_SRVR = 210102,

/*! The contacted feature is a Perpetual/Repository License. */
   SNTL_PERPETUAL_OR_REPOSITORY_LICENSE = 210103,

/*! A commuter token has already been checked out for this license. */
   SNTL_COMMUTER_CHECKOUT = 210104,

/*! License with given feature/version is either not available on the server
    * or belongs to a different vendor. */
   SNTL_REVOKE_ERR_NO_FEATURE = 210105,

/*! The message received by the server was corrupted. */
   SNTL_REVOKE_ERR_CORRUPT_MESSAGE = 210106,

/*! The received number of licenses to revoke out of range. */
   SNTL_REVOKE_ERR_OUT_VALID_RANGE = 210107,

/*! Error loading the MD5 plugin DLL at the server. */
   SNTL_REVOKE_ERR_MD5_PLUGIN_LOAD_FAIL = 210108,

/*! Error in executing the authentication plugin. */
   SNTL_REVOKE_ERR_MD5_PLUGIN_EXEC_FAIL = 210109,

/*! This feature has less number of total licenses. */
   SNTL_REVOKE_ERR_INSUFFICIENT_FEATURE_LICENSES = 210110,

/*! Default group does not has sufficient licenses,
*   reconfigure your user.  */
   SNTL_REVOKE_ERR_INSUFFICIENT_DEFAULT_GROUP = 210111,

/*! Currently required number of licenses are not free for revoke in the
*   default group. */
   SNTL_REVOKE_ERR_INSUFFICIENT_FREE_IN_DEFAULT = 210112,

/*! Invalid SessionID sent by the client in packet. */
   SNTL_REVOKE_ERR_INVALID_SESSION_ID = 210113,

/*! Invalid password for revocation. */
   SNTL_REVOKE_ERR_INVALID_PASSWORD = 210114,

/*! Revocation failed due to internal server error. */
   SNTL_REVOKE_ERR_INTERNAL_SERVER = 210115,

/*! Infinite revoke not possible with enabled group distribution. */
   SNTL_REVOKE_ERR_INFINITE_GRP_DIST = 210116,

/*! All licenses must be free for infinite revocation. */
   SNTL_REVOKE_ERR_INFINITE_LIC_IN_USE = 210117,

/*! License has infinite keys. Only infinite license revocation request is
*   allowed for this license.  */
   SNTL_REVOKE_ERR_INFINITE_LIC_FINITE_REQ = 210118,

/*! Permission Ticket generation for revoke license failed. */
   SNTL_REVOKE_ERR_TICKET_GENERATION = 210119,

/*! Revocation feature is not supported for the specified license version. */
   SNTL_REVOKE_ERR_CODGEN_VERSION_UNSUPPORTED = 210120,

/*! Revocation feature is not supported for redundant licenses. */
   SNTL_REVOKE_ERR_RDNT_LIC_UNSUPPORED = 210121,

/*! Unexpected challenge packet received from server. */
   SNTL_REVOKE_ERR_UNEXPECTED_AUTH_CHLG_PKT = 210123,

/*! Revocation feature is not supported for trial licenses. */
   SNTL_REVOKE_ERR_TRIAL_LIC_UNSUPPORED = 210124,

/*! Not all required lock selectors are available. */
   SNTL_REQUIRED_LOCK_FIELDS_NOT_FOUND = 210125,

/*! Total lock selectors available is less than minimum number. */
   SNTL_NOT_ENOUGH_LOCK_FIELDS = 210126,

/*! Remote checkout is not allowed for perpetual and repository licenses. */
   SNTL_REMOTECHECKOUT_NOT_ALLOWED_PERPETUAL_OR_REPOSITORY = 210127,

/*! Installation of grace license on client machine failed. */
   SNTL_GRACE_LIC_INSTALL_FAIL = 210128,

/*! The feature is not supported in the No-Net lib/mode of the server. */
   SNTL_NOT_SUPPORTED_IN_NONET_LIBRARY_OR_MODE = 210129,

/*! No active client handle exists. */
   SNTL_NO_ACTIVE_HANDLE = 210130,

/*! Library is not in initialized state. */
   SNTL_LIBRARY_NOT_INITIALIZED = 210131,

/*! Library is already in initialized state. */
   SNTL_LIBRARY_ALREADY_INITIALIZED = 210132,

/*! Fail to acquire API lock. API call should be re-tried on receiving this error. */
   SNTL_RESOURCE_LOCK_FAILURE = 210133,

/*! No install location is set. */
   SNTL_INSTALL_STORE_NOT_SET = 210134,

/*! No more license stores. */
   SNTL_NO_MORE_LICENSE_STORES = 210135,

/*! No such license store. */
   SNTL_NO_SUCH_LICENSE_STORE = 210136,

/*! License store is full. */
   SNTL_LICENSE_STORE_FULL = 210137,

/*! Specified size of store is too small. */
   SNTL_STORE_SIZE_TOO_SMALL = 210138,

/*! No more licenses. */
   SNTL_NO_MORE_LICENSES = 210139,

/*! No license found with the specified feature/version/hash. */
   SNTL_NO_SUCH_LICENSE = 210140,

/*! License is in use and have active clients. */
   SNTL_LICENSE_IN_USE = 210141,

/*! Failure in setting the precedence for the specified trial license. */
   SNTL_SET_LICENSE_PRECEDENCE_FAILED = 210142,

/*! Failure in accessing the license or persistence store. */
   SNTL_STORE_ACCESS_ERROR = 210143,

/*! Corruption in store. */
   SNTL_STORE_DATA_INCONSISTENT = 210144,

/*! Unable to create/open the store. */
   SNTL_STORE_OPEN_ERROR = 210145,

/*! License store query failed. */
   SNTL_LICENSE_STORE_QUERY_FAILED = 210146,

/*! Specified lock selector is not valid. */
   SNTL_LOCK_SELECTOR_INVALID = 210147,

/*! The specified locking code is not supported. */
   SNTL_LOCK_CODE_NOT_SUPPORTED = 210148,

/*! Invalid lock code version. */
   SNTL_LOCK_CODE_VER_INVALID = 210149,

/*! Invalid lock code. */
   SNTL_LOCK_CODE_INVALID = 210150,

/*! No available fingerprint for specified lock selector. */
   SNTL_NO_AVAILABLE_MACHINE_ID = 210151,

/*! Code generator library initialization failed. */
   SNTL_CODE_GENERATOR_LIBRARY_FAILED = 210152,

/*! The specified trial feature is not accessible. */
   SNTL_TRIAL_LIC_DATA_ACCESS_ERROR = 210153,

/*! Trial License data inconsistent for this feature. */
   SNTL_TRIAL_LIC_DATA_INCONSISTENT = 210154,

/*! Trial license date restriction error for this feature. */
   SNTL_TRIAL_LIC_DATE_RESTRICTED = 210155,

/*! A disabled trial license is requested. */
   SNTL_TRIAL_LIC_NOT_ACTIVATED = 210156,

/*! Failure in calling sequence of the API. */
   SNTL_CALL_SEQUENCE_ERROR = 210157,

/*! Specified record doesn't exit in the store. */
   SNTL_RECORD_NOT_FOUND = 210158,

/*! No more record available in the store. */
   SNTL_NO_MORE_RECORDS = 210159,

/*! The license was not processed in the specified operation. */
   SNTL_LICENSE_NOT_PROCESSED = 210160,

/*! Given configuration is not allowed. */
   SNTL_CONFIGURATION_NOT_ALLOWED = 210161,

/*! Value exceeds the maximum size for the field. */
   SNTL_EXCEEDS_MAX_SIZE = 210162,

/*! Value specified is not within the valid range. */
   SNTL_VALUE_OUT_OF_RANGE = 210163,

/*! A user without administrator privileges called the VLSinitialize API
 *  when persistence is not initialized on the system. */
   SNTL_PERSISTENCE_CONFIGURATION_ERROR = 210164,

/*! A network request is made to the standalone library. */
   SNTL_NONET_LIBRARY = 210165,

/*! The store with specified name already exists. */
   SNTL_STORE_ALREADY_EXISTS = 210166,

/*! Failure in specifying the backup information correctly. */
   SNTL_BACKUP_CONFIGURATION_ERROR = 210167,

/*! Record in license/trial/revocation store is corrupt. */
   SNTL_RECORD_CORRUPT = 210168,

/*! Specified record in license store is empty. */
   SNTL_LICENSE_RECORD_EMPTY = 210169,

/*! Failure in writing to file in save license API. */
   SNTL_SAVE_LICENSE_FILE_WRITE_ERROR = 210170,

/*! File already exists in save license API. */
   SNTL_SAVE_LICENSE_FILE_ALREADY_EXISTS = 210171,

/*! Persistence store is full. */
   SNTL_PERSISTENCE_STORE_FULL = 210172,

/*! Cleaning is not required on the current store as it is already in good state. */
   SNTL_CLEAN_REPAIR_NOT_REQUIRED = 210173,

/*! Cleaning attempted more than twice on the same persistence context object. */
   SNTL_CLEAN_REPAIR_ATTEMPTED = 210174,

/*! Persistence store is un-recoverable when repairing/cleaning is tried. */
   SNTL_CLEAN_NOT_RECOVERABLE = 210175,

/*! Persistence store is not relevant. */
   SNTL_CLEAN_WRONG_FILE = 210176,

/*! Unable to clean/repair. */
   SNTL_CLEAN_REPAIR_FAIL = 210177,

/*! All data is lost in cleaning, i.e. no recovery. */
   SNTL_CLEAN_REPAIR_COMPLETE_LOSS = 210178,

/*! Partial recovery taken place on cleaning. */
   SNTL_CLEAN_REPAIR_WITH_LOSS = 210179,

/*! License is not client locked. */
   SNTL_LICENSE_NOT_LOCKED = 210180,

/*! License has not expired and has valid lock code or is unlocked. */
   SNTL_LICENSE_NOT_EXPIRED_AND_HAS_VALID_LOCK_CODE = 210181,

/*! Mismatch between the specified lock code. */
   SNTL_LOCK_CODE_MISMATCH = 210182,

/*! Handler function is already registered. */
   SNTL_HANDLER_ALREADY_REGISTERED = 210183,

/*! Specified license is not a trial one. */
   SNTL_NON_TRIAL_LICENSE = 210184,

/*! License addition cancelled by callback. */
   SNTL_ADD_LIC_CANCELLED_BY_USER = 210185,

/*! Neither any active handle nor any pending cache update exists. */
   SNTL_NO_UPDATE_REQUIRED = 210186,

/*! This license has already been revoked. */
   SNTL_LICENSE_ALREADY_REVOKED = 210187,

/*! License start date not yet reached. */
   SNTL_LICENSE_START_DATE_NOT_REACHED = 210188,

/*! Buffer too small. */
   SNTL_REHOST_BUFFER_TOO_SMALL = 210193,

/*! Buffer too small, it must not happen. */
   SNTL_REHOST_BUFFER_TOO_SMALL_UNEXPECTED = 210194,

/*! Invalid rehost parameters. */
   SNTL_REHOST_PARAMETERS_ERROR = 210195,

/*! Algorithm not supported. */
   SNTL_REHOST_UNSUPPORTED_ALGO = 210196,

/*! Invalid tlv data format. */
   SNTL_REHOST_INVALID_DATA_FORMAT = 210197,

/*! Invalid rehost request data. */
   SNTL_REHOST_INVALID_REQUEST_DATA = 210198,

/*! Operation type not supported. */
   SNTL_REHOST_UNSUPPORTED_OPERATION_TYPE = 210199,

/*! Memory allocation failure. */
   SNTL_REHOST_ALLOCATE_MEMORY_FAILURE = 210200,

/*! Tag can not be found in tlv. */
   SNTL_REHOST_TAG_NOT_FOUND = 210201,

/*! Lock code mismatching. */
   SNTL_REHOST_DIFFERENT_LOCK_INFO = 210202,

/*! License to be revoked is in use, can not be revoked. */
   SNTL_REHOST_LICENSE_IN_USE = 210203,

/*! Something unexpected has occurred. */
   SNTL_REHOST_UNEXPECTED_ERROR = 210204,

/*! The license has already been revoked. */
   SNTL_REHOST_HAVE_BEEN_REVOKED_BEFORE = 210205,

/*! Revocation request exceeds the available limit. */
   SNTL_REHOST_REVOKE_OVER_TOTAL = 210206,

/*! License already exists. */
   SNTL_REHOST_LICENSE_EXIST = 210207,

/*! Revoke option was cancelled by the user. */
   SNTL_REHOST_CANCELED_BY_USER = 210208,

/*! Rehost status is not defined. */
   SNTL_REHOST_STATUS_NOT_DEFINED = 210209,

/*! Grace code length exceeds maximum limit. */
   SNTL_GRACE_CODE_LENGTH_OVERFLOW_ERROR = 210210,

/*! No more fingerprint information is available. */
   SNTL_ERROR_NO_MORE_FINGERPRINT_VALUE = 210211,

/*! No more fingerprint information is available on specified index. */
   SNTL_ERROR_FINGERPRINT_NOT_FOUND = 210212,

/*! License deletion is not supported for grace licenses, redundant 
*   licenses and checked out licenses. */
   SNTL_LICENSE_DELETION_NOT_ALLOWED = 210213,

/*! Commuter code is expired. */
   SNTL_EXPIRED_COMMUTER_CODE = 210215,

/*! Commuter code start date is not reached. */
   SNTL_COMMUTER_CODE_DATE_RESTRICTED = 210216,

/*! If the limit value has been updated by any other process after the current process
*   has retrieved the limit value. */
   SNTL_NEW_RECORD_FOUND = 210217,

/*! No records for the limit in the database. */
   SNTL_NO_RECORDS_FOUND = 210218,

/*! The requested operation failed for any other reason. */
   SNTL_OPERATION_NOT_SUCCESSFUL = 210219,

/*! Included for restricting commuter checkout to primary leader server. */
   SNTL_ERROR_READING_SERVER_CONFIG_FILE = 210220,

/*! Licenses can't be checked out only from the primary License Manager. */
   SNTL_CHECKOUT_NOT_ALLOWED_FROM_NONPRIMARY_LEADER = 210221,

/*! Standalone revocation is supported for V11 licenses only. */
   SNTL_REHOST_LIC_VERSION_NOT_SUPPORTED = 210222,

/*! The usage log file is tampered. */
   SNTL_USAGE_FILE_TAMPERED = 210223,

/*! The matching record is not found in the usage log file. */
   SNTL_NO_MATCH_FOUND = 210224,

/*! TCPIP protocol version specified for client library is incorrect. */
   SNTL_INVALID_TCPIP_VERSION = 210225,

/*! The License Manager is being run on a virtual machine. */
   SNTL_VIRTUAL_MACHINE_IS_DETECTED = 210226,

/*! The system initialization failed for a grace license. */
   SNTL_GRACE_LIC_TIME_TAMPER_INIT_FAIL = 210227,

/*! Persistence is either corrupt or doesn't exist. */
   SNTL_REVOKE_LIC_DATA_INCONSISTENT = 210228,

/*! Permission ticket size is more than supported length,
*   operations should be reduced from PT. */
   SNTL_TOO_MANY_OPERATIONS_IN_SINGLE_PT = 210229,

/*! Permission ticket operation already executed on the server. */
   SNTL_PT_ALREADY_EXECUTED_FOR_THIS_OPERATION = 210230,

/*! Vendor ID mismatch of permission ticket. */
   SNTL_PT_VENDOR_ID_MISMATCH = 210231,

/*! Expired License can not be added or revoked. */
   SNTL_REVOKE_EXPIRED_LIC_FOUND = 210232,

/*! Commuter code checkout not allowed for this feature. */
   SNTL_COMMUTER_CHECKOUT_NOT_ALLOWED = 210233,

/*! Application can not run on Remote desktop session. */
   SNTL_RDP_SESSION_FOUND = 210234,

/*! Not enough keys are available to check out commuter code for given duration. */
   SNTL_NOT_ENOUGH_COMMUTER_KEYS_FOR_DURATION = 210235,

/*! Old permission tickets are not supported in new network revocation. */
   SNTL_REHOST_UNSUPPORTED_PT_VERSION = 210236,

/*! A deferred revocation has been performed successfully. */
   SNTL_DEFERRED_REVOCATION_SUCCESS = 210237,

/*! A deferred revocation request has already been executed for this license. */
   SNTL_LIC_ALREADY_SCHEDULED_FOR_DEFERRED_REVOKE = 210238,

/*! Commuter checkout and repository request not allowed after 
*   deferred revocation operation is performed on a feature-version.  */
   SNTL_OPERATION_NOT_ALLOWED_AFTER_DEFERRED_REVOCATION = 210239,

/*! Deferred revocation is not allowed in case commuter keys already 
 *  issued against the feature-version * or repository license is already requested. */
   SNTL_DEFERRED_REVOCATION_NOT_ALLOWED = 210240,

/*! Logging backup disabled because '-x' option is specified at LM server startup. */
   SNTL_USAGE_LOG_BACKUP_DISABLED = 210241,

/*! Either persistence is corrupted or doesn't exist. */
   SNTL_COMMUTER_DATA_INCONSISTENT = 210242,

/*! For vendor isolation - client not communicating with intended server. */
   SNTL_NON_INTENDED_SERVER_CONTACTED = 210243,

/*! Operation is not permitted on the follower server. */
   SNTL_OPERATION_ONLY_ALLOWED_ON_LEADER_SERVER = 210244,

/*! Insufficient tokens available at server to increase during license update. */
   SNTL_LICENSE_UPGRADE_DENIED = 210245,

/*! The signing key index of the requested license is lower than the one sent by the client. */
   SNTL_LOWER_SIGNING_KEYINDEX_IN_LIC = 210248,

/*! The feature being returned was commuted by different mechanism.*/
   SNTL_INCOMPATIBLE_COMMUTER_CODE = 210250,

/*! The latest commuter code is already installed. */
   SNTL_COMMUTER_CODE_TOO_OLD = 210251,

/* The lease license is already cancelled. */
   SNTL_LEASE_LICENSE_CANCELLED = 210252,

/* Sync lease license is in progress. */
   SNTL_LEASE_INPROGRESS = 210253,

/* Lease license is cancelled from client only.*/
   SNTL_CANCELLED_FROM_CLIENT = 210254,

/* SCC communication failure. */
   SNTL_SCC_COMMUNICATION_FAILED = 210255,

/*! Input handle is associated to zombie session and is invalid to use in this API*/
   SNTL_ZOMBIE_LOGIN_SESSION = 210256,
   
/*!User session terminated */
   SNTL_USER_SESSION_TERMINATED = 210257,

/*! Either fingerprint friendly name has been used before or machine 
 *  fingerprint has changed. */
   SNTL_SCC_MACHINE_FINGERPRINT_CHANGED = 210258, 

/*! Fingerprint friendly name does not exist on SCC. */
   SNTL_SCC_MACHINE_NOT_FOUND = 210259,

/*! Customer does not exist on SCC. */
   SNTL_SCC_CUSTOMER_NOT_FOUND = 210260, 

/*! Non Cloud license added on cloud lm */
   SNTL_NONCLOUD_LIC_ADDED_ON_CLOUD_LM = 210261,
   
/*! The feature is not supported in the cloudlm mode. */
   SNTL_NOT_SUPPORTED_IN_CLOUDLM_MODE = 210262,

/*! cloudlm mode is not supported in non-scp integrated library. */
   SNTL_CLOUDLM_MODE_NOT_SUPPORTED_IN_NONSCP_LIBRARY = 210263,

/*! Clock of client machine is skewed. */
   SNTL_CLOCK_SKEW_ERROR = 210264,
   
/*! Invalid Login Session. */
   SNTL_INVALID_LOGIN_SESSION = 214097,

/*! Not enough licensing resources are available to satisfy the request. */
   SNTL_INSUFFICIENTUNITS = 214098,

/*! No licensing system could be found with which to perform the function
*   invoked. */
   SNTL_LICENSESYSNOTAVAILABLE = 214099,

/*! The licensing system has determined that the resources used to satisfy
*   a previous request are no longer granted to the calling application. */
   SNTL_LICENSETERMINATED = 214100,

/*! The licensing system has no licensing resources that could satisfy the request. */
   SNTL_NOAUTHORIZATIONAVAILABLE = 214101,

/*! All licensing tokens for the specified feature are already in use. */
   SNTL_NOLICENSESAVAILABLE = 214102,

/*! Insufficient resources (such as memory) are available to complete the
*   request. */
   SNTL_NORESOURCES = 214103,

/*! The network is unavailable. */
   SNTL_NO_NETWORK = 214104,

/*! A warning occurred while looking up an error message string for the
*   LSGetMessage() function. */
   SNTL_NO_MSG_TEXT = 214105,

/*! An unrecognised status code was passed into the LSGetMessage() function. */
   SNTL_UNKNOWN_STATUS = 214106,

/*! An invalid index has been specified. */
   SNTL_BAD_INDEX = 214107,

/*! No more units are available. */
   SNTL_NO_MORE_UNITS = 214108,

/*! Feature cannot run any more because the license expiration date has reached. */
   SNTL_LICENSE_EXPIRED = 214109,

/*! Input buffer is too small, need a bigger buffer. */
   SNTL_BUFFER_TOO_SMALL = 214110, 

/*! Failed in performing the requisite operation. */
   SNTL_NO_SUCCESS = 214111, 

/*! Grace Days have been used up. */
   SNTL_GRACE_EXPIRED = 214112,

/*! Unexpected state of Grace License. */
   SNTL_GRACE_INVALID_STATE = 214113,

/*! Grace Hours have been used up. */
   SNTL_GRACE_HOURS_EXHAUSTED = 214114,

/*! Licensing system could not locate enough available licensing resources
*   on the follower server. */
   SNTL_INSUFFICIENTUNITS_ON_FOLLOWER = 214115,

/*! Invalid Application Context. */
   SNTL_INVALID_APP_CONTEXT = 220001,

/*! Invalid Attribute Key. */
   SNTL_INVALID_ATTR_KEY = 220002,

/*! Invalid Attribute Value. */
   SNTL_INVALID_ATTR_VALUE = 220003,   

/*! Attribute Deprecated. */
   SNTL_DEPRECATED_ATTR = 220004,

/*! Active Login Session Exist Value. */
   SNTL_ACTIVE_LOGIN_SESSION_EXIST = 220005,
   
};

typedef unsigned int       sntl_uint32_t;

/*! Status type */
typedef enum sntl_status_codes sntl_status_t;

/*! Application Context */
typedef void sntl_licensing_app_context_t;

/*! Login Session*/
typedef void sntl_licensing_login_session_t;

/*! Attribute */
typedef void sntl_licensing_attr_t;

/*! Identity */
typedef void sntl_licensing_identity_t;

/*! Callback */
typedef long (* sntl_licensing_callback_t) (char *, char *, unsigned int *);
/**
* @}
*/


/**
* @defgroup attrib_related_APIs Attribute related APIs
* @{
*/

/**
* \brief            Creates a new attribute object.
*
* \param            attr      [out] Points to the attribute object created.
*   						  Memory resources shall be allocated by the API 
*							  and can be released using sntl_licensing_attr_delete().
*
* \return           SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_attr_new(sntl_licensing_attr_t **attr);

/**
* \brief            Sets values in the attribute object.
*
* \param            attr      [in] The attribute object in which the "value" is to be set based on the "key".
* \param            key       [in] The "key" based on which "value" would be set.
*            e.g., SNTL_ATTR_APPCONTEXT_CONTACT_SERVER is one of the keys for an application context object.
* \param            value     [in] The "value" to be set.
*            e.g., "localhost" can be a valid value for the key SNTL_ATTR_APPCONTEXT_CONTACT_SERVER.
*
* \return           SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_attr_set(sntl_licensing_attr_t *attr,
                                    const char *key,
                                    const char *value);

/**
* \brief            API to set an attribute object in another attribute object.
*
* \return           SNTL_SUCCESS if successful, otherwise, an appropriate error code when an 
*                   attribute that is not meant to be passed to the set object variant.
*
* \note             This API does not support any attribute for now
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t)  sntl_licensing_attr_set_object (sntl_licensing_attr_t *attr, const char *key, sntl_licensing_attr_t *value);


/**
* \brief            API to add an attribute object in another attribute object.
*
* \param            attr      [in] The attribute object in which the "value" is to be set based on the "key".
* \param            key       [in] The "key" based on which "value" would be set.
*            e.g., SNTL_ATTR_CONFIG_SCP_PRODUCT_KEY_LIST  is one of the keys for customer object.
* \param            value     [in] The "value" to be set.
*            e.g., The attribute object of which the "value" is to be set in the attribute object "attr".
*
* \return           SNTL_SUCCESS if successful, otherwise, an appropriate error code when an 
*                   attribute that is not meant to be passed to the set object variant.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t)  sntl_licensing_attr_add_object (sntl_licensing_attr_t *attr, const char *key, sntl_licensing_attr_t *value);

/*! \brief          Deletes the attribute object.
*
* \param            attr      [in] The attribute object to be deleted.
*
* \return           SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(void) sntl_licensing_attr_delete(sntl_licensing_attr_t *attr);
/**
* @}
*/


#define SNTL_ATTR_YES                    "yes"
#define SNTL_ATTR_NO                     "no"

/* Possible values for 'type' parameter in sntl_licensing_register_callback(). */
#define SNTL_CALLBACK_TYPE_CUSTOM_FINGERPRINT    "customFingerprint"
#define SNTL_CALLBACK_TYPE_CUSTOM_TRACE_WRITER 	 "customTraceWriter"

/*! \brief          Register a callback for customizing the default behaviour provided by the library.
*
* \param            app_context  [in] This parameter should be NULL; it is reserved for future needs 
* \param            type         [in] Define the purpose for which callback is being registered.
*                                     See SNTL_CALLBACK_TYPE_CUSTOM_FINGERPRINT and SNTL_CALLBACK_TYPE_CUSTOM_TRACE_WRITER.
* \param            call_back    [in] Implementation of callback being registered.
*
* \return           SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_register_callback(sntl_licensing_app_context_t *app_context, 
									         char *type,
									         const sntl_licensing_callback_t call_back);


/**
* @defgroup config_APIs Library Configuration API and Macros
* @{
*/

#define SNTL_ATTR_CONFIG_TRACE_WRITER_FILE              "config_trace_writer_file"
#define SNTL_ATTR_CONFIG_TRACE_LEVEL                    "config_trace_level"
#define SNTL_ATTR_CONFIG_LSERVRC_FILE                   "config_lservrc_file"
#define SNTL_ATTR_CONFIG_SCP_USE_CONFIG_FILE            "config_scp_use_config_file"
#define SNTL_ATTR_CONFIG_SCP_YPS_ADDRESS                "config_scp_yps_address"
#define SNTL_ATTR_CONFIG_SCP_TENANT_HOST_ADDRESS        "config_scp_tenant_host_address"
#define SNTL_ATTR_CONFIG_SCP_FINGERPRINT_FRIENDLYNAME   "config_scp_fingerprint_friendlyname"
#define SNTL_ATTR_CONFIG_SCP_CONNECTION_TIMEOUT         "config_scp_connection_timeout"
#define SNTL_ATTR_CONFIG_SCP_CONNECTION_RETRY_COUNT     "config_scp_connection_retry_count"
#define SNTL_ATTR_CONFIG_SCP_PROXY_MODE                 "config_scp_proxy_mode"
#define SNTL_ATTR_CONFIG_SCP_PROXY_HOST                 "config_scp_proxy_host"
#define SNTL_ATTR_CONFIG_SCP_PROXY_USER                 "config_scp_proxy_user"
#define SNTL_ATTR_CONFIG_SCP_PROXY_PASSWORD             "config_scp_proxy_password"
#define SNTL_ATTR_CONFIG_SCP_PROXY_PORT                 "config_scp_proxy_port"
#define SNTL_ATTR_CONFIG_SCP_PROXY_PAC                  "config_scp_proxy_pac"
#define SNTL_ATTR_CONFIG_SCP_PKID                       "config_scp_pkid"
#define SNTL_ATTR_CONFIG_SCP_PRODUCT_VARIANT            "config_scp_product_variant"
#define SNTL_ATTR_CONFIG_SCP_PRODUCT_QUANTITY           "config_scp_product_quantity"
#define SNTL_ATTR_CONFIG_SCP_CUSTOMERID                 "config_scp_customerid"
#define SNTL_ATTR_CONFIG_SCP_REGISTRATION_TOKEN         "config_scp_registration_token"

/*Macros for sntl_licensing_attr_add_object API */
#define SNTL_ATTR_CONFIG_SCP_PRODUCT_KEY_LIST           "config_scp_product_key_list"
#define SNTL_ATTR_CONFIG_SCP_CUSTOMER_LIST              "config_scp_customer_key_list"

/* Possible values for attribute 'SNTL_ATTR_CONFIG_TRACE_LEVEL' used by the library. */
#define SNTL_ATTR_CONFIG_TRACE_FUNCTION             "trace_function"
#define SNTL_ATTR_CONFIG_TRACE_ERROR                "trace_error"

/* Macros for setting attributes for sntl_licensing_configure(). */
#define sntl_licensing_attr_set_config_trace_writer_file(_attr, _value) \
sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_TRACE_WRITER_FILE , _value)

#define sntl_licensing_attr_set_config_trace_level(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_TRACE_LEVEL, _value) /* SNTL_ATTR_CONFIG_TRACE_FUNCTION or SNTL_ATTR_CONFIG_TRACE_ERROR */

#define sntl_licensing_attr_set_config_lservrc_file(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_LSERVRC_FILE, _value)

#define sntl_licensing_attr_set_config_scp_use_config_file(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_USE_CONFIG_FILE, _value)

#define sntl_licensing_attr_set_config_scp_yps_address(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_YPS_ADDRESS, _value)

#define sntl_licensing_attr_set_config_scp_tenant_host_address(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_TENANT_HOST_ADDRESS, _value)
   
#define sntl_licensing_attr_set_config_scp_fingerprint_friendlyname(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_FINGERPRINT_FRIENDLYNAME, _value)

#define sntl_licensing_attr_set_config_scp_connection_timeout(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_CONNECTION_TIMEOUT, _value)

#define sntl_licensing_attr_set_config_scp_connection_retry_count(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_CONNECTION_RETRY_COUNT, _value)

#define sntl_licensing_attr_set_config_scp_proxy_mode(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_PROXY_MODE, _value)

#define sntl_licensing_attr_set_config_scp_proxy_host(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_PROXY_HOST, _value)

#define sntl_licensing_attr_set_config_scp_proxy_user(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_PROXY_USER, _value)

#define sntl_licensing_attr_set_config_scp_proxy_password(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_PROXY_PASSWORD, _value)

#define sntl_licensing_attr_set_config_scp_proxy_port(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_PROXY_PORT, _value)

#define sntl_licensing_attr_set_config_scp_proxy_pac(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_PROXY_PAC, _value)

#define sntl_licensing_attr_set_config_scp_pkid(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_PKID, _value)

#define sntl_licensing_attr_set_config_scp_product_variant(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_PRODUCT_VARIANT, _value)

#define sntl_licensing_attr_set_config_scp_product_quantity(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_PRODUCT_QUANTITY, _value)

#define sntl_licensing_attr_set_config_scp_customerid(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_CUSTOMERID, _value)
   
#define sntl_licensing_attr_set_config_scp_registration_token(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_CONFIG_SCP_REGISTRATION_TOKEN, _value)

#define sntl_licensing_attr_add_object_scp_product_key_list(_attr, _value) \
   sntl_licensing_attr_add_object(_attr, SNTL_ATTR_CONFIG_SCP_PRODUCT_KEY_LIST, _value)

#define sntl_licensing_attr_add_object_scp_customer_list(_attr, _value) \
   sntl_licensing_attr_add_object(_attr, SNTL_ATTR_CONFIG_SCP_CUSTOMER_LIST, _value)

/*! \brief      	Performs library configuration defined by the attribute object parameter.
*
* \param        	attr         [in] The attribute object.
*
* \return       SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark       For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_configure(const sntl_licensing_attr_t *attr);

/**
* @}
*/


/**
* @defgroup app_context_MACROs_APIs Application Context related APIs and Macros
* @{
*/

/* Possible values for attribute 'SNTL_ATTR_APPCONTEXT_CONTROL_REMOTE_SESSION' used by app_context. */
#define SNTL_CONTROL_REMOTE_BOTH_TYPES      "disallow-terminal-disallow-rdp"
#define SNTL_CONTROL_REMOTE_ONLY_TERMINAL   "disallow-terminal-allow-rdp"
#define SNTL_CONTROL_REMOTE_NONE            "allow-terminal-allow-rdp"

#define SNTL_ERROR_FILE_NONE             "none"
#define SNTL_ERROR_FILE_STDOUT           "stdout"
#define SNTL_ERROR_FILE_STDERR           "stderr"

/* Possible values for attribute 'SNTL_ATTR_APPCONTEXT_MINIMUM_SIGNING_KEY_INDEX' used by app_context. */

/* Signing key index for restricting license consumption to the more secure RSA signed licenses (version 18 and above). */
#define SNTL_RSA_SIGNING_KEY_INDEX         "1"
#define SNTL_DEFAULT_SIGNING_KEY_INDEX     SNTL_RSA_SIGNING_KEY_INDEX
/* Signing key index for allowing consumption of licenses of all versions,including the AES encrypted licenses (version 17 and below). */
#define SNTL_AES_SIGNING_KEY_INDEX         "0"

/* Macro for setting CloudLM mode as contact server */
#define SNTL_CLOUDLM                       "sntl-cloudlm"

#define SNTL_ATTR_APPCONTEXT_CONTACT_SERVER               "appcontext_contact_server"
#define SNTL_ATTR_APPCONTEXT_NETWORK_TIMEOUT              "appcontext_network_timeout"
#define SNTL_ATTR_APPCONTEXT_CONTROL_REMOTE_SESSION       "appcontext_control_remote_session"
#define SNTL_ATTR_APPCONTEXT_REQUEST_GRACE                "appcontext_request_grace"
#define SNTL_ATTR_APPCONTEXT_ENABLE_LOCAL_RENEWAL         "appcontext_enable_local_renewal"
#define SNTL_ATTR_APPCONTEXT_HOSTNAME                     "appcontext_hostname"
#define SNTL_ATTR_APPCONTEXT_SERVER_PORT                  "appcontext_server_port"
#define SNTL_ATTR_APPCONTEXT_BROADCAST_INTERVAL           "appcontext_broadcast_interval"
#define SNTL_ATTR_APPCONTEXT_DEFAULT_ERROR_HANDLER        "appcontext_default_error_handler"
#define SNTL_ATTR_APPCONTEXT_AUTO_REFRESH                 "appcontext_auto_refresh"
#define SNTL_ATTR_APPCONTEXT_XDISPLAYNAME                 "appcontext_xdisplayname"
#define SNTL_ATTR_APPCONTEXT_VENDOR_DEFINED_SHARINGID     "appcontext_vendor_defined_sharingid"
#define SNTL_ATTR_APPCONTEXT_MINIMUM_SIGNING_KEY_INDEX    "appcontext_minimum_signing_key_index"
#define SNTL_ATTR_APPCONTEXT_CONTACT_SERVER_LIST 		  "appcontext_contact_server_list"
#define SNTL_ATTR_APPCONTEXT_ENABLE_EXHAUSTIVE_BROADCAST  "appcontext_enable_exhaustive_broadcast"

/* Macros for setting attributes for application context. */
#define sntl_licensing_attr_set_appcontext_contact_server(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_APPCONTEXT_CONTACT_SERVER, _value)

#define sntl_licensing_attr_set_appcontext_timeout_interval(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_APPCONTEXT_NETWORK_TIMEOUT, _value)

#define sntl_licensing_attr_set_appcontext_remote_session_flag(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_APPCONTEXT_CONTROL_REMOTE_SESSION, _value)

#define sntl_licensing_attr_set_appcontext_request_grace_flag(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_APPCONTEXT_REQUEST_GRACE, _value)

#define sntl_licensing_attr_set_appcontext_local_renewal_flag(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_APPCONTEXT_ENABLE_LOCAL_RENEWAL, _value)

#define sntl_licensing_attr_set_appcontext_hostname(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_APPCONTEXT_HOSTNAME, _value)

#define sntl_licensing_attr_set_appcontext_server_port(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_APPCONTEXT_SERVER_PORT, _value)

#define sntl_licensing_attr_set_appcontext_broadcast_interval(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_APPCONTEXT_BROADCAST_INTERVAL, _value)

#define sntl_licensing_attr_set_appcontext_default_error_handler(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_APPCONTEXT_DEFAULT_ERROR_HANDLER, _value)

#define sntl_licensing_attr_set_appcontext_auto_refresh(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_APPCONTEXT_AUTO_REFRESH, _value)

#define sntl_licensing_attr_set_appcontext_xdisplayname(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_APPCONTEXT_XDISPLAYNAME, _value)

#define sntl_licensing_attr_set_appcontext_vendor_defined_sharingid(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_APPCONTEXT_VENDOR_DEFINED_SHARINGID, _value)

#define sntl_licensing_attr_set_appcontext_minimum_signing_key_index(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_APPCONTEXT_MINIMUM_SIGNING_KEY_INDEX, _value)
 
#define sntl_licensing_attr_set_appcontext_contact_server_list(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_APPCONTEXT_CONTACT_SERVER_LIST , _value)
   
#define sntl_licensing_attr_set_appcontext_enable_exhaustive_broadcast(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_APPCONTEXT_ENABLE_EXHAUSTIVE_BROADCAST  , _value)

/*! \brief          Creates the Application Context object.
*
* \param            vendor_id      [in]  For future use, '0' may be passed.
* \param            attr           [in]  The (optional) attribute object.
* \param            app_context    [out] Points to the application context object created.
*                                  Memory resources shall be allocated by the API 
*                                  and can be released using sntl_licensing_app_context_delete().
*
* \return           SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_app_context_new(sntl_uint32_t vendor_id,
                                    sntl_licensing_attr_t *attr,
                                    sntl_licensing_app_context_t **app_context);


/*! \brief          Deletes the Application Context object.
*
* \param            app_context    [in] The application context object to be deleted.
*
* \return           SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_app_context_delete(sntl_licensing_app_context_t *app_context);

/* End of application-context related APIs. */

/**
* @}
*/

/**
* @defgroup identity_APIs Identity related APIs and Macros
* @{
*/

#define SNTL_ATTR_IDENTITY_USERNAME      		   "identity_username"

#define sntl_licensing_attr_set_identity_username(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_IDENTITY_USERNAME, _value)


/*! \brief          Creates the identity object based on the configuration provided through the "attr" parameter.
*
* \param            app_context    [in]  The application context object. 
* \param            attr           [in]  The (optional) attribute object.
* \param            identity       [out] Pointer to the identity object created. Memory resources shall be allocated by the API 
*                                  and can be released using sntl_licensing_identity_delete(). 
*
* \return           SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_identity_new(sntl_licensing_app_context_t *app_context,
                                    const sntl_licensing_attr_t *attr,
                                    sntl_licensing_identity_t **identity);


/*! \brief          Converts the identity object to the readable string stream. 
*
*                   This string-stream "identity_string" can be set in the "attr" param of sntl_licensing_login_attr()
*                   OR sntl_licensing_transfer() using the keys SNTL_ATTR_LOGIN_IDENTITY_STRING or 
*                   SNTL_ATTR_TRANSFER_IDENTITY_STRING respectively.
*
* \param            identity             [in]  The identity object.
* \param            identity_string      [out] Pointer to the string stream created. 
*                       Memory resources shall be allocated by the API and can be released using sntl_licensing_free(). 
*
* \return           SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_identity_serialize(const sntl_licensing_identity_t *identity,
                                    char **identity_string);


/*! \brief          Deletes the identity object.
*
* \param            identity    [in] The identity object to be deleted.
*
* \return           SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(void) sntl_licensing_identity_delete(sntl_licensing_identity_t *identity);


/**
* @}
*/



/**
* @defgroup session_Macros_APIs Basic Licensing APIs and related Macros
* @{
*/

/*! \brief          Requests license for the feature name specified.
*
* \param            app_context        [in] The application context object.
* \param            feature_name       [in] The feature for which license is being requested.
* \param            login_session      [out] Points to the handle of the session created.
*                   Memory resources shall be allocated by the API 
*                   and get released during the sntl_licensing_logout() call.
*
* \return           SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_login(sntl_licensing_app_context_t *app_context,
                               const char *feature_name,
                               sntl_licensing_login_session_t **login_session);



/* Attribute keys for sntl_licensing_login_attr. */
#define SNTL_ATTR_LOGIN_FEATURE_VERSION                "login_feature_version"
#define SNTL_ATTR_LOGIN_UNITS_REQUIRED                 "login_units_required"
#define SNTL_ATTR_LOGIN_VENDOR_USAGE_DATA              "login_vendor_usage_data"
#define SNTL_ATTR_LOGIN_CHALLENGE_SECRET               "login_challenge_secret"
#define SNTL_ATTR_LOGIN_CHALLENGE_DATA                 "login_challenge_data"
#define SNTL_ATTR_LOGIN_VENDOR_ISOLATION_IDENTIFIER    "login_vendor_isolation_identifier"
#define SNTL_ATTR_LOGIN_IGNORE_GRACE_ERROR             "login_ignore_grace_error" 			/* SNTL_ATTR_YES or SNTL_ATTR_NO */
#define SNTL_ATTR_LOGIN_IDENTITY_STRING                "login_identity_string"
#define SNTL_ATTR_LOGIN_USAGE_COUNT_MULTIPLIER         "login_usage_count_multiplier"
#define SNTL_ATTR_LOGIN_DISABLE_GRACE_BROADCAST        "login_disable_grace_broadcast" 	/* SNTL_ATTR_YES */
#define SNTL_ATTR_LOGIN_ZOMBIE_SESSION                 "login_zombie_session" /*SNTL_ATTR_YES*/
#define SNTL_ATTR_LOGIN_ZOMBIE_SESSION_IDENTIFIER_MASK "login_zombie_session_identifier_mask"

/* Possible values for attribute 'SNTL_ATTR_LOGIN_ZOMBIE_SESSION_IDENTIFIER_MASK' used by login for cleanup */
#define SNTL_ZOMBIE_SESSION_IDENTIFIER_HOSTNAME              1      /*0x1*/
#define SNTL_ZOMBIE_SESSION_IDENTIFIER_USERNAME              2      /*0x2*/
#define SNTL_ZOMBIE_SESSION_IDENTIFIER_MACHINE_FINGERPRINT   4      /*0x4*/
#define SNTL_ZOMBIE_SESSION_IDENTIFIER_ALL                   (SNTL_ZOMBIE_SESSION_IDENTIFIER_HOSTNAME | SNTL_ZOMBIE_SESSION_IDENTIFIER_USERNAME | SNTL_ZOMBIE_SESSION_IDENTIFIER_MACHINE_FINGERPRINT)

/* Macros for setting attributes for sntl_licensing_login_attr. */
#define sntl_licensing_attr_set_feature_version(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_LOGIN_FEATURE_VERSION, _value)

#define sntl_licensing_attr_set_login_units_required(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_LOGIN_UNITS_REQUIRED, _value)

#define sntl_licensing_attr_set_login_vendor_usage_data(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_LOGIN_VENDOR_USAGE_DATA, _value)

#define sntl_licensing_attr_set_login_challenge_secret(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_LOGIN_CHALLENGE_SECRET, _value)

#define sntl_licensing_attr_set_login_challenge_data(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_LOGIN_CHALLENGE_DATA, _value)

#define sntl_licensing_attr_set_login_vendor_isolation_identifier(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_LOGIN_VENDOR_ISOLATION_IDENTIFIER, _value)

#define sntl_licensing_attr_set_login_ignore_grace_error(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_LOGIN_IGNORE_GRACE_ERROR, _value)

#define sntl_licensing_attr_set_login_identity_string(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_LOGIN_IDENTITY_STRING, _value)
   
#define sntl_licensing_attr_set_login_usage_count_multiplier(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_LOGIN_USAGE_COUNT_MULTIPLIER, _value)
   
#define sntl_licensing_attr_set_login_disable_grace_broadcast(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_LOGIN_DISABLE_GRACE_BROADCAST, _value)
   
#define sntl_licensing_attr_set_login_create_zombie_session(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_LOGIN_ZOMBIE_SESSION, _value)
   
#define sntl_licensing_attr_set_login_create_zombie_session_identifier_mask(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_LOGIN_ZOMBIE_SESSION_IDENTIFIER_MASK, _value)
   
/* END of defines for sntl_licensing_login_attr. */

/*! \brief          Requests license for the feature name specified based on the configurations set by the "attr" parameter.
*
* \param            app_context        [in] The application context object. 
* \param            feature_name       [in] The feature for which license is being requested.
* \param            attr               [in] The (optional) attribute object.
* \param            login_session      [out] Points to the handle of the session created.
*                   Memory resources shall be allocated by the API and gets released during the sntl_licensing_logout() call.
*
* \return           SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_login_attr(sntl_licensing_app_context_t *app_context,
                                    const char *feature_name,                        
                                    const sntl_licensing_attr_t *attr,               
                                    sntl_licensing_login_session_t **login_session);


/*! \brief      Renews the license obtained through sntl_licensing_login() OR sntl_licensing_login_attr().
*
* \param        login_session      		[in] The session handle created via sntl_licensing_login() OR sntl_licensing_login_attr().
*
* \return       SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark       For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_refresh(sntl_licensing_login_session_t *login_session);


/* Attribute keys for sntl_licensing_refresh_attr. */
#define SNTL_ATTR_REFRESH_VENDOR_USAGE_DATA              "refresh_vendor_usage_data"
#define SNTL_ATTR_REFRESH_CHALLENGE_SECRET               "refresh_challenge_secret"
#define SNTL_ATTR_REFRESH_CHALLENGE_DATA                 "refresh_challenge_data"
#define SNTL_ATTR_REFRESH_GRACE_SWITCH_TIME              "refresh_grace_switch_time"
#define SNTL_ATTR_REFRESH_UNITS_REQUIRED                 "refresh_units_required"
#define SNTL_ATTR_REFRESH_USAGE_COUNT_MULTIPLIER         "refresh_usage_count_multiplier"


/* Macros for setting attributes for sntl_licensing_refresh_attr. */

#define sntl_licensing_attr_set_refresh_vendor_usage_data(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_REFRESH_VENDOR_USAGE_DATA, _value)

#define sntl_licensing_attr_set_refresh_challenge_secret(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_REFRESH_CHALLENGE_SECRET, _value)

#define sntl_licensing_attr_set_refresh_challenge_data(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_REFRESH_CHALLENGE_DATA, _value)


#define sntl_licensing_attr_set_refresh_grace_switch_time(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_REFRESH_GRACE_SWITCH_TIME, _value)
   
#define sntl_licensing_attr_set_refresh_units_required(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_REFRESH_UNITS_REQUIRED, _value)

#define sntl_licensing_attr_set_refresh_usage_count_multiplier(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_REFRESH_USAGE_COUNT_MULTIPLIER, _value)
/* END of defines for sntl_licensing_refresh_attr. */


/*! \brief      Renews the license obtained through sntl_licensing_login() OR 
*               sntl_licensing_login_attr() API based on the configurations set by the "attr" parameter.
*
* \param        login_session      [in] The session handle created via sntl_licensing_login() OR sntl_licensing_login_attr().
* \param        attr               [in] The (optional) attribute object.
*
* \return       SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark       For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_refresh_attr(sntl_licensing_login_session_t *login_session,
									         const sntl_licensing_attr_t *attr);


/*! \brief      Frees the license (and its associated memory resources) obtained through 
*                   sntl_licensing_login() OR sntl_licensing_login_attr() API.
*
* \param        login_session      [in] The session handle created via sntl_licensing_login() OR sntl_licensing_login_attr().
*
* \return       SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark       For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_logout(sntl_licensing_login_session_t *login_session);



/* Attribute keys for sntl_licensing_logout_attr. */
#define SNTL_ATTR_LOGOUT_VENDOR_USAGE_DATA           "logout_vendor_usage_data"
#define SNTL_ATTR_LOGOUT_UNITS_TO_RELEASE            "logout_units_to_release"
#define SNTL_ATTR_LOGOUT_USAGE_COUNT_MULTIPLIER      "logout_usage_count_multiplier"

/* Macros for setting attributes for sntl_licensing_logout_attr. */

#define sntl_licensing_attr_set_logout_vendor_usage_data(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_LOGOUT_VENDOR_USAGE_DATA, _value)

#define sntl_licensing_attr_set_logout_units_to_release(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_LOGOUT_UNITS_TO_RELEASE, _value)
   
#define sntl_licensing_attr_set_logout_usage_count_multiplier(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_LOGOUT_USAGE_COUNT_MULTIPLIER, _value)

/* END of defines for sntl_licensing_logout_attr. */

/*! \brief      Frees the license (and its associated memory resources) obtained through sntl_licensing_login() OR
*                   sntl_licensing_login_attr() API based on the configurations set by the "attr" parameter.
*
* \param        login_session      [in] The session handle created via sntl_licensing_login() OR sntl_licensing_login_attr().
* \param        attr               [in] The (optional) attribute object.
*
* \return       SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark       For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_logout_attr(sntl_licensing_login_session_t *login_session,
                                    const sntl_licensing_attr_t *attr);

/**
* @} 
*/

/**
* @defgroup query_APIs Information Retrieval APIs
* @{
*/

#define SNTL_SESSIONINFO                 "<sentinelQuery query=\"sessionInfo\"/>"

/*! \brief      Introduced in 9.5.0 to support query based on incremental versions.
*   \param      v       [in] version text as quoted string; should be "1.1" until next increment.
*/
#define SNTL_SESSIONINFO_VERSION(v)      "<sentinelQuery query=\"sessionInfo\" version=\"" v "\"/>"

/*! \brief      Introduced in 9.5.0 , this macro point to latest version of query.
*/
#define SNTL_SESSIONINFO_LATEST          SNTL_SESSIONINFO_VERSION("1.1")


/*! \brief      Retrieves information about the license/session obtained through 
*                   sntl_licensing_login() OR sntl_licensing_login_attr().
*
* \param        login_session   [in] The session handle created via sntl_licensing_login() OR sntl_licensing_login_attr().
* \param        query           [in] Currently, only one type of query "SNTL_SESSIONINFO" is supported.
* \param        info            [out] Pointer to the buffer containing XML-based output.
*                               Memory resources shall be allocated by the API and can be released using sntl_licensing_free().
*
* \return       SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark       For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_get_session_info(sntl_licensing_login_session_t *login_session,
                                    const char *query,
                                    char **info);

/* Macros specifying the "scope" parameter for sntl_licensing_get_info(). */
#define SNTL_QUERY_SCOPE_NONE  "<sentinelScope/>"

/* Macros specifying the "query" parameter for sntl_licensing_get_info().
* Default version for below queries is 1.0. Following macros are kept for backward compatibility.
* ISVs are suggested to use macros suffixed with _VERSION.
*/
#define SNTL_QUERY_FEATURE_INFO                           "<sentinelQuery query=\"featureInfo\"/>"
#define SNTL_QUERY_LICENSE_INFO                           "<sentinelQuery query=\"licenseInfo\"/>"
#define SNTL_QUERY_CLIENT_INFO                            "<sentinelQuery query=\"clientInfo\"/>"
#define SNTL_QUERY_LIBRARY_INFO                           "<sentinelQuery query=\"libraryInfo\"/>"
#define SNTL_QUERY_RECIPIENT_INFO                         "<sentinelQuery query=\"recipientInfo\"/>"
#define SNTL_QUERY_FINGERPRINT_INFO                       "<sentinelQuery query=\"fingerprintInfo\"/>"
#define SNTL_QUERY_APPCONTEXT_INFO                        "<sentinelQuery query=\"appContextInfo\"/>"
#define SNTL_QUERY_SERVER_INFO                            "<sentinelQuery query=\"serverInfo\"/>"
#define SNTL_QUERY_FEATURE_CUMULATIVE_TRIAL_INFO          "<sentinelQuery query=\"featureCumulativeTrialInfo\"/>"
#define SNTL_QUERY_SERVERPOOL_INFO                        "<sentinelQuery query=\"serverPoolInfo\"/>"

/* Refer documentation for the supported versions. 
*  Version should be passed in double quotes,
*  e.g SNTL_QUERY_FEATURE_INFO_VERSION("1.0").
*/
#define SNTL_QUERY_FEATURE_INFO_VERSION(v)                           "<sentinelQuery query=\"featureInfo\" version=\"" v "\"/>"
#define SNTL_QUERY_LICENSE_INFO_VERSION(v)                           "<sentinelQuery query=\"licenseInfo\" version=\"" v "\"/>"
#define SNTL_QUERY_CLIENT_INFO_VERSION(v)                            "<sentinelQuery query=\"clientInfo\" version=\"" v "\"/>"
#define SNTL_QUERY_LIBRARY_INFO_VERSION(v)                           "<sentinelQuery query=\"libraryInfo\" version=\"" v "\"/>"
#define SNTL_QUERY_RECIPIENT_INFO_VERSION(v)                         "<sentinelQuery query=\"recipientInfo\" version=\"" v "\"/>"
#define SNTL_QUERY_FINGERPRINT_INFO_VERSION(v)                       "<sentinelQuery query=\"fingerprintInfo\" version=\"" v "\"/>"
#define SNTL_QUERY_APPCONTEXT_INFO_VERSION(v)                        "<sentinelQuery query=\"appContextInfo\" version=\"" v "\"/>"
#define SNTL_QUERY_SERVER_INFO_VERSION(v)                            "<sentinelQuery query=\"serverInfo\" version=\"" v "\"/>"
#define SNTL_QUERY_FEATURE_CUMULATIVE_TRIAL_INFO_VERSION(v)          "<sentinelQuery query=\"featureCumulativeTrialInfo\" version=\"" v "\"/>"
#define SNTL_QUERY_SERVERPOOL_INFO_VERSION(v)                        "<sentinelQuery query=\"serverPoolInfo\" version=\"" v "\"/>"
#define SNTL_QUERY_SYNC_LICENSE_JOB_INFO_VERSION(v)                  "<sentinelQuery query=\"syncLicenseJobInfo\" version=\"" v "\"/>"
#define SNTL_QUERY_LOCK_CODE_INFO_VERSION(v)                         "<sentinelQuery query=\"lockCodeInfo\" version=\"" v "\"/>"
#define SNTL_QUERY_LAST_STATUS_INFO_VERSION(v)                       "<sentinelQuery query=\"lastStatusInfo\" version=\"" v "\"/>"
#define SNTL_QUERY_STATUS_INFO_VERSION(v)                            "<sentinelQuery query=\"statusInfo\" version=\"" v "\"/>"
#define SNTL_QUERY_USAGE_INFO_VERSION(v)                             "<sentinelQuery query=\"usageInfo\" version=\"" v "\"/>"


/*! \brief      Introduced in 9.5.0 , these macros point to latest version of corresponding queries.
*/
#define SNTL_QUERY_FEATURE_INFO_LATEST                               SNTL_QUERY_FEATURE_INFO_VERSION("1.1")
#define SNTL_QUERY_LICENSE_INFO_LATEST                               SNTL_QUERY_LICENSE_INFO_VERSION("1.1")
#define SNTL_QUERY_CLIENT_INFO_LATEST                                SNTL_QUERY_CLIENT_INFO_VERSION("1.1")
#define SNTL_QUERY_LIBRARY_INFO_LATEST                               SNTL_QUERY_LIBRARY_INFO_VERSION("1.0")
#define SNTL_QUERY_RECIPIENT_INFO_LATEST                             SNTL_QUERY_RECIPIENT_INFO_VERSION("1.0")
#define SNTL_QUERY_FINGERPRINT_INFO_LATEST                           SNTL_QUERY_FINGERPRINT_INFO_VERSION("1.1")
#define SNTL_QUERY_APPCONTEXT_INFO_LATEST                            SNTL_QUERY_APPCONTEXT_INFO_VERSION("1.0")
#define SNTL_QUERY_SERVER_INFO_LATEST                                SNTL_QUERY_SERVER_INFO_VERSION("1.0")
#define SNTL_QUERY_FEATURE_CUMULATIVE_TRIAL_INFO_LATEST              SNTL_QUERY_FEATURE_CUMULATIVE_TRIAL_INFO_VERSION("1.0")
#define SNTL_QUERY_SERVERPOOL_INFO_LATEST                            SNTL_QUERY_SERVERPOOL_INFO_VERSION("1.0")
#define SNTL_QUERY_SYNC_LICENSE_JOB_INFO_LATEST                      SNTL_QUERY_SYNC_LICENSE_JOB_INFO_VERSION("1.0")
#define SNTL_QUERY_LOCK_CODE_INFO_LATEST                             SNTL_QUERY_LOCK_CODE_INFO_VERSION("1.0")
#define SNTL_QUERY_LAST_STATUS_INFO_LATEST                           SNTL_QUERY_LAST_STATUS_INFO_VERSION("1.0")
#define SNTL_QUERY_STATUS_INFO_LATEST                                SNTL_QUERY_STATUS_INFO_VERSION("1.0")
#define SNTL_QUERY_USAGE_INFO_LATEST                                 SNTL_QUERY_USAGE_INFO_VERSION("1.0")

/*! \brief      Retrieves information based on the "query" parameter passed.
*
* Based on the "query" parameter, the following types of information can be retrieved using this API:
*
*   featureInfo
*   licenseInfo
*   clientInfo
*   libraryInfo
*   recipientInfo
*   fingerprintInfo
*   appContextInfo
*   serverInfo
*   featureCumulativeTrialInfo
*   serverPoolInfo
*   syncLicenseJobInfo
*   lockCodeInfo
*   lastStatusInfo
*   statusInfo
*   usageInfo
*
* \param        app_context   [in] The application context object. 
* \param        scope         [in] The "scope" for the "query" being made. Refer to the 'API Reference Guide' document for details.
* \param        query         [in] The "query" type, e.g., SNTL_QUERY_FEATURE_INFO, SNTL_QUERY_LICENSE_INFO etc.
* \param        info          [out] Pointer to the buffer containing XML-based output.
*                               Memory resources shall be allocated by the API and can be released using sntl_licensing_free().
*
* \return       SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark       For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_get_info(sntl_licensing_app_context_t *app_context,
									         const char *scope,
									         const char *query,
									         char **info);

/**
* @}
*/

/**
* @defgroup transfer_install_API Transfer and Install License APIs and related Macros
* @{
*/

/* Macros for setting a particular locking criterion.
*  To be used in the SNTL_ATTR_TRANSFER_LOCK_MASK attribute for sntl_licensing_transfer(). */
#define SNTL_LOCK_ID_PROM               1   /*0x1*/
#define SNTL_LOCK_IP_ADDR               2   /*0x2*/
#define SNTL_LOCK_DISK_ID               4   /*0x4*/
#define SNTL_LOCK_HOSTNAME              8   /*0x8*/
#define SNTL_LOCK_ETHERNET             16   /*0x10*/
#define SNTL_LOCK_PORTABLE_SERV       128   /*0x80*/
#define SNTL_LOCK_CUSTOM              256   /*0x100*/
#define SNTL_LOCK_CUSTOMEX           1024   /*0x400*/
#define SNTL_LOCK_HARD_DISK_SERIAL   2048   /*0x800*/
#define SNTL_LOCK_CPU_INFO           4096   /*0x1000*/
#define SNTL_LOCK_UUID               8192   /*0x2000*/
#define SNTL_LOCK_ALL                (SNTL_LOCK_ID_PROM | SNTL_LOCK_IP_ADDR | SNTL_LOCK_DISK_ID | SNTL_LOCK_HOSTNAME | SNTL_LOCK_ETHERNET | SNTL_LOCK_PORTABLE_SERV | SNTL_LOCK_CUSTOM | SNTL_LOCK_CUSTOMEX | SNTL_LOCK_HARD_DISK_SERIAL | SNTL_LOCK_CPU_INFO | SNTL_LOCK_UUID )

#define SNTL_ATTR_TRANSFER_UNITS_REQUIRED                    "transfer_units_required"
#define SNTL_ATTR_TRANSFER_VENDOR_USAGE_DATA                 "transfer_vendor_usage_data"
#define SNTL_ATTR_TRANSFER_LOCK_MASK                         "transfer_lock_mask"
#define SNTL_ATTR_TRANSFER_EXTENSION_IN_DAYS                 "transfer_extension_in_days"
#define SNTL_ATTR_TRANSFER_IDENTITY_STRING                   "transfer_identity_string"

/* Macros for setting attributes for sntl_licensing_transfer(). */
#define sntl_licensing_attr_set_transfer_units_required(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_TRANSFER_UNITS_REQUIRED, _value)

#define sntl_licensing_attr_set_transfer_vendor_usage_data(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_TRANSFER_VENDOR_USAGE_DATA, _value)

#define sntl_licensing_attr_set_transfer_lock_mask(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_TRANSFER_LOCK_MASK, _value)

#define sntl_licensing_attr_set_transfer_extension_in_days(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_TRANSFER_EXTENSION_IN_DAYS, _value)

#define sntl_licensing_attr_set_transfer_identity_string(_attr, _value) \
   sntl_licensing_attr_set(_attr, SNTL_ATTR_TRANSFER_IDENTITY_STRING, _value)


/*! \brief      Performs commuter code checkout from the License Manager.
*
* \param        app_context   [in] The application context object. 
* \param        action        [in] Defines the "commute" / "sync" / "cancelLease" / "resumeLease" / "readyUsageForUpload" operation. For details, refer to the 'API Reference Guide' document.
* \param        scope         [in] For future use, pass NULL for now.
* \param        attr          [in] The (optional) attribute object.
* \param        recipient     [in] Defines the machine-ID string of remote client/machine to 
*                                  which commuter code shall be issued.
*                                  To retrieve the "recipient" information, use sntl_licensing_get_info(). 
* \param        license       [out] Pointer to the commuter code buffer.
*           Memory resources shall be allocated by the API and can be released using sntl_licensing_free().
*
* \return       SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark       This API is deprecated from 9.2.0 onwards, new API sntl_licensing_transfer() can be used to perform similar operation.
* \remark       For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_transfer_license(sntl_licensing_app_context_t *app_context,
                                        const char *action,
                                        const char *scope,
                                        const sntl_licensing_attr_t *attr,
                                        const char *recipient,
                                        char **license);


/*! \brief      Installs license (normal/commuter) on the License Manager/client machine (respectively).
*               Also, perform permission ticket based revocation of licenses.
*
* If the "license" parameter is a regular license string, the license shall be installed on the License Manager.
* If it is the commuter-code from sntl_licensing_transfer(), it shall be installed on the machine where this is executed.
*
* \param        app_context   [in]  The application context object.
* \param        license       [in]  The license/permission_ticket to be installed/executed.
* \param        attr          [in]  For future use, pass NULL for now.
* \param        acknowledge   [out] Returns revocation ticket.
*
* \return       SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark       This API is deprecated from 9.2.0 onwards, new API sntl_licensing_install() can be used to perform similar operation.
* \remark       For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_install_license(sntl_licensing_app_context_t *app_context,
                                    const char *license,
                                    const sntl_licensing_attr_t *attr,
                                    char **acknowledge);

/*! \brief      Uninstall/Delete given license from the License Manager based on either license string or hash.
* If the license string corresponding to license hash is available at License Manager, then the license shall be deleted from the License Manager and license store.
*
* \param        app_context     [in]  The application context object.
* \param        uninstall_data  [in]  Pointer to the XML-based input buffer containing license string or hash.
* \param        status          [out] Pointer to the XML-based output buffer containing license string or hash.
*
* \return       SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark       For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_uninstall(sntl_licensing_app_context_t *app_context,
                                    const char *uninstall_data,
                                    char **status);

/*! \brief      Performs commuter code checkout from the License Manager.
*
* \param        app_context   [in] The application context object. 
* \param        action        [in] Defines the "commute" / "sync" / "cancelLease" / "resumeLease" / "readyUsageForUpload" operation. For details, refer to the 'API Reference Guide' document.
* \param        scope         [in] For future use, pass NULL for now.
* \param        attr          [in] The (optional) attribute object.
* \param        recipient     [in] Defines the machine-ID string of remote client/machine to 
*                                  which commuter code shall be issued.
*                                  To retrieve the "recipient" information,use sntl_licensing_get_info().
* \param        info          [out] Pointer to the commuter code buffer.
*           Memory resources shall be allocated by the API and can be released using sntl_licensing_free().
*
* \return       SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark       For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_transfer(sntl_licensing_app_context_t *app_context,
                                        const char *action,
                                        const char *scope,
                                        const sntl_licensing_attr_t *attr,
                                        const char *recipient,
                                        char **info);

/*! \brief      Installs license (normal/commuter) on the License Manager/client machine (respectively).
*               Also, perform permission ticket based revocation of licenses.
*
* If the "license" parameter is a regular license string, the license shall be installed on the License Manager.
* If it is the commuter-code from sntl_licensing_transfer(), it shall be installed on the client machine.
*
* \param        app_context   [in]  The application context object.
* \param        install_data  [in]  The license/permission_ticket to be installed/executed.
* \param        attr          [in]  For future use, pass NULL for now.
* \param        acknowledge   [out] Returns revocation ticket.
*
* \return       SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark       For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_install(sntl_licensing_app_context_t *app_context,
                                    const char *install_data,
                                    const sntl_licensing_attr_t *attr,
                                    char **acknowledge);

/**
* @}
*/


/**
* @defgroup free_cleanup_API Free and Cleanup APIs
* @{
*/

/*! \brief     Frees the memory resources allocated to storing retrieved data from API calls. 
*
* \param       buffer      [in] Pointer to the memory resources allocated by any of the following APIs:
*   <ul>
*     <li>sntl_licensing_get_session_info()</li>
*     <li>sntl_licensing_get_info()</li>
*     <li>sntl_licensing_transfer()</li>
*     <li>sntl_licensing_identity_serialize()</li>
*   </ul>
* \return      This is a void function.
*
* \remark      For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(void) sntl_licensing_free(void *buffer);



/*! \brief          Performs library level cleanup.
*
* \return           SNTL_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_status_t) sntl_licensing_cleanup();

/**
 * @}
 */

/**
* @defgroup deprecated APIs MACROs VALUEs etc.
* @{
*/

/*! \brief     This section contains information about API 's attributes, related macros 
*              which have been renamed/improved interfaces.
*
* \remark      These details are put here to give quick hints to developers if their build breaks after 
*              SDK version upgrade.
*/

/* 
*
*

Type - Macro
Old Name - SNTL_ATTR_APPCONTEXT_TRACE_LEVEL
New Name - Removed completely. The macros for possible values (SNTL_TRACE_LICENSE, SNTL_TRACE_FUNCTION, SNTL_TRACE_ERROR, SNTL_TRACE_ALL) have also been removed.
Changed in SDK version - RMS 9.3.0
Note: Instead use the updated functionality provided via sntl_licensing_configure API.
      For legacy applications, the string "appcontext_trace_level" can be used instead of the SNTL_ATTR_APPCONTEXT_TRACE_LEVEL macro.

Type - Macro
Old Name - SNTL_ATTR_LOGOUT_UNITS_CONSUMED
New Name - SNTL_ATTR_LOGOUT_UNITS_TO_RELEASE
Behavioural differences - None
Changed in SDK version - RMS 9.1.0

Type - Macro
Old Name - SNTL_ATTR_LOGIN_VENDOR_IDENTIFIER
New Name - SNTL_ATTR_LOGIN_VENDOR_ISOLATION_IDENTIFIER
Behavioural differences - None
Changed in SDK version - RMS 9.1.0

Type - Macro
Old Name - SNTL_ATTR_LOGIN_CHALLENGE_SIZE
New Name - Removed completely
Behavioural differences - Not Applicable
Changed in SDK version - RMS 9.1.0

Type - Macro
Old Name - SNTL_ATTR_REFRESH_CHALLENGE_SIZE
New Name - Removed completely
Behavioural differences - Not Applicable
Changed in SDK version - RMS 9.1.0

Type - Macro
Old Name - SNTL_MAX_VER_LEN
New Name - SNTL_MAX_FEATURE_VERSION_LEN
Behavioural differences - Not Applicable
Changed in SDK version - RMS 9.1.0

Type - Macro
Old Name - SNTL_MAX_FEA_LEN
New Name - SNTL_MAX_FEATURE_NAME_LEN
Behavioural differences - Not Applicable
Changed in SDK version - RMS 9.1.0

Type - Macro
Old Name - SNTL_VENDOR_USAGE_DATA_LEN
New Name - SNTL_MAX_VENDOR_USAGE_DATA_LEN
Behavioural differences - Not Applicable
Changed in SDK version - RMS 9.1.0

Type - Macro
Old Name - SNTL_VENDOR_IDENTIFIER_LEN
New Name - SNTL_MAX_VENDOR_IDENTIFIER_LEN
Behavioural differences - Not Applicable
Changed in SDK version - RMS 9.1.0

Type - Macro
Old Name - SNTL_MAX_BUF_LEN
New Name - Removed completely
Behavioural differences - Not Applicable
Changed in SDK version - RMS 9.1.0

Type - Macro
Old Name - SNTL_CUSTOM_DATA_FIELD_SIZE
New Name - SNTL_MAX_CUSTOM_HOSTNAME_LEN, SNTL_MAX_IDENTITY_USERNAME_LEN 
Behavioural differences - Not Applicable
Changed in SDK version - RMS 9.1.0


*
*
*/



#ifdef __cplusplus
} // extern "C"
#endif

#endif /* #define SNTL_LICENSING_H */

/*End of File */
