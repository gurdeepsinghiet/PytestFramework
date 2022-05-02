/*******************************************************************/
/*                                                                 */
/*                 Copyright (C) 2021 Thales Group                 */
/*                       All Rights Reserved.                      */
/*                                                                 */
/*     This Module contains Proprietary Information of Thales      */
/*          Group, and should be treated as Confidential.          */
/*******************************************************************/

/**
 * \mainpage Sentinel Persistence Management APIs
 * \file lspmgmtinit.h Sentinel Persistence Management API 
 *  declarations
 */

#ifndef _LSPMGMTINIT_H
#define _LSPMGMTINIT_H

/* H****************************************************************
* FILENAME    : lspmgmtinit.h
*
* DESCRIPTION :
*           Contains public function prototypes, macros and defines
*           needed for Persistence Management.
* USAGE       :
*           This file should be included by the developer who is 
*           creating applications that are being used to create or 
*           manage persistence used by licensed application.
*
*H*/

#ifdef __cplusplus
extern "C" {
#endif

#define SNTL_PMGMT_COPYRIGHT_STR    "  Copyright (C) 2021 Thales Group\n       All Rights Reserved.\n\n"

#define SNTL_DECLARE(_type)                _type  

/*! Sentinel Status Codes */
enum sntl_persistence_status_codes
{
/*! The function executed successfully. */
   SNTL_PERSISTENCE_SUCCESS = 0, 

/*! Failed in performing the requisite operation. */
   SNTL_PERSISTENCE_NO_SUCCESS = 510001,

/*! Fail to acquire API lock. API call should be re-tried on receiving this error. */
   SNTL_PERSISTENCE_RESOURCE_LOCK_FAILURE = 510002,

/*! The requested operation is not supported in this library. */
   SNTL_PERSISTENCE_NOT_SUPPORTED = 510003,

/*! Error in calling API. */    
   SNTL_PERSISTENCE_CALLING_ERROR = 510004,

/*! Insufficient resources (such as memory) are available to complete the operation. */
   SNTL_PERSISTENCE_NO_RESOURCES = 510005,
    
/*! Invalid persistence Context. */
   SNTL_PERSISTENCE_INVALID_CONTEXT = 510006,

/*! DEPRECATED - Please use SNTL_PERSISTENCE_INSUFFICIENT_PERMISSIONS. */
   SNTL_PERSISTENCE_INSUFFICIENT_PERMISIONS = 510007,

/*! User do not have sufficient permission to complete the operation. */
   SNTL_PERSISTENCE_INSUFFICIENT_PERMISSIONS = 510007,

/*! Failed while performing persistence configuration. */
   SNTL_PERSISTENCE_CONFIG_FAIL = 510008,

/*! Persistence information already exists. */
   SNTL_PERSISTENCE_FILE_INFO_EXISTS = 510009,

/*! Error reading persistence file. */
   SNTL_PERSISTENCE_FILE_READ_FAIL = 510010,

/*! Error writing into persistence file. */
   SNTL_PERSISTENCE_FILE_WRITE_FAIL = 510011,

/*! Error opening persistence file. */
   SNTL_PERSISTENCE_FILE_OPEN_FAIL = 510012,

/*! Error getting lock. */
   SNTL_PERSISTENCE_LOCK_ERROR = 510013,

/*! File not found. */
   SNTL_PERSISTENCE_FILE_NOT_FOUND = 510014,

/*! Internal error. */
   SNTL_PERSISTENCE_INTERNAL_ERROR = 510015,
   
/*! *Library Not Initialized. */
   SNTL_PERSISTENCE_LIBRARY_NOT_INITIALIZED = 510016,

/*! Invalid Attribute Key. */
   SNTL_PERSISTENCE_INVALID_ATTR_KEY = 510017,

/*! Library is not serialized with the vendor Id . */ 
   SNTL_PERSISTENCE_VENDOR_ID_ERROR = 510018,

/*!Persistence Device Type is not supported. */
   SNTL_PERSISTENCE_DEVICE_NOT_SUPPORTED = 510019,

/*! File or persistence database tampered. */ 
   SNTL_PERSISTENCE_FILE_TAMPERED  = 510020,

/*! Error in writing Persistence database. */ 
   SNTL_PERSISTENCE_UNABLE_TO_WRITE  = 510021,

/*! Unable to write Persistence DB. */ 
   SNTL_PERSISTENCE_FILE_ACCESS_ERROR =  510022,

/*! No data can be recovered from the database. */ 
   SNTL_PERSISTENCE_NOT_RECOVERABLE = 510023,

/*! Database not found for this vendor. */
   SNTL_PERSISTENCE_WRONG_FILE = 510024,

/*! Inconsistent persistence record found. */
   SNTL_PERSISTENCE_BAD_RECORD_SIZE = 510025,

/*! Repair has not been performed on this database. */ 
   SNTL_PERSISTENCE_REPAIR_NOT_PERFORMED  = 510026,

/*! Unable to repair Persistence file/database.*/
   SNTL_PERSISTENCE_REPAIR_FAIL = 510027,

/*! Database repaired with complete data loss. */
   SNTL_PERSISTENCE_REPAIR_COMPLETE_LOSS = 510028,

/*! Database repaired with some data loss occurred. */
   SNTL_PERSISTENCE_REPAIR_WITH_LOSS = 510029,

/*! Mismatch in the primary and backup file. */
   SNTL_PERSISTENCE_MISMATCH_FILES =  510030,

/*! Repair already attempted on this database.*/
   SNTL_PERSISTENCE_REPAIR_ATTEMPTED = 510031,

/*! Unable to access Persistence primary file/database.*/
   SNTL_PERSISTENCE_PATH_ACCESS_ERROR = 510032,

/*! DEPRECATED - Please use SNTL_PERSISTENCE_DB_NOT_INITIALIZED. */
   SNTL_PERSISTENCE_DB_NOT_INITILIZED = 510033,

/*! Persistence database initialization error. */
   SNTL_PERSISTENCE_DB_NOT_INITIALIZED = 510033,

/*! Unable to protect Persistence file/database.*/
   SNTL_PERSISTENCE_DB_NOT_SECURED = 510034,

/*! Persistence record not found.*/
   SNTL_PERSISTENCE_RECORD_NOT_FOUND = 510035,
   
/*! Persistence invalid input or parameter error. */
   SNTL_PERSISTENCE_INTERNAL_PARAMETER_ERROR = 510036,

/*! Persistence files are already secured. */
   SNTL_PERSISTENCE_ALREADY_SECURED = 510037,

/*! Persistence authentication error. */
   SNTL_PERSISTENCE_AUTH_DATA_ERROR = 510038,

/*! Max limit for available resources has been reached. */
   SNTL_PERSISTENCE_MAX_LIMIT_REACHED_ERROR = 510039,

/*! Out of resource Error.*/
   SNTL_PERSISTENCE_MAX_RESOURCE_LIMIT_ERROR = 510040,

/*! Persistence File handler error. */
   SNTL_PERSISTENCE_FILE_HANDLE_ERROR = 510041,

/*! Persistence internal path too long.*/
   SNTL_PERSISTENCE_PATH_TOO_LONG = 510042,

/*! Error in accessing persistence section. */
   SNTL_PERSISTENCE_SECTION_ACCESS_ERROR = 510043,

/*! Persistence section not available. */
   SNTL_PERSISTENCE_INVALID_SECTION = 510044,

/*! Persistence section not found. */
   SNTL_PERSISTENCE_INVALID_SECTION_VERSION = 510045,

/*! Persistence DB Inconsistent.*/ 
   SNTL_PERSISTENCE_DATA_INCONSISTENT =  510046,

/*! Persistence DB does not exist.*/ 
   SNTL_PERSISTENCE_DB_DOES_NOT_EXIST =  510047,

/*! No commuter record in the persistence DB */
   SNTL_PERSISTENCE_NO_COMMUTER_FEATURE_VERSION_IN_USE =  510048,

/*! No records found in the persistence DB*/ 
   SNTL_PERSISTENCE_NO_RECORDS_FOUND =  510049
};

typedef enum sntl_persistence_status_codes sntl_persistence_status_t;

/*! Attribute */
typedef void sntl_persistence_attr_t;

/*! Persistence Context */
typedef void sntl_persistence_context_t;

/*! \brief          Creates a new attribute object.
*                   Currently, no attributes are supported.
*                   API for future releases.
*
* \param            attr      [out] Points to the attribute object 
*                             created. Memory resources shall be 
*                             allocated by the API and can be 
*                             released using 
*                             sntl_persistence_attr_delete().
*
* \return           SNTL_PERSISTENCE_SUCCESS if successful, otherwise, 
*                   an appropriate error code.
*
* \remark           For further information, please refer to the 
*                   'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_persistence_status_t) sntl_persistence_attr_new(
                                           sntl_persistence_attr_t **attr);

/*! \brief          Sets values in the attribute object.
*                   Currently, no attributes are supported.
*                   API for future releases.
*
* \param            attr      [in] The attribute object in which the
*                   "value" is to be set based on the "key".
* \param            key       [in] The "key" based on which "value" 
*                   would be set.
* \param            value     [in] The "value" to be set.
*
* \return           SNTL_PERSISTENCE_SUCCESS if successful, 
*                   otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 
*                   'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_persistence_status_t) sntl_persistence_attr_set(
                                           sntl_persistence_attr_t *attr,
                                           const char              *key,
                                           const char              *value);

/*! \brief          Deletes the attribute object.
*                   Currently, no attributes are supported.
*                   API for future releases.
*
* \param            attr      [in] The attribute object to be 
*                   deleted.
*
* \return           void.
*
* \remark           For further information, please refer to the 
*                   'API Reference Guide' document.
*/
SNTL_DECLARE(void) sntl_persistence_attr_delete(sntl_persistence_attr_t *attr);

/*! Device type */

/*! Device type */
enum sntl_persistence_device
 {
   SNTL_PERSISTENCE_NO_DEVICE                = 0, /* Not Supported currently. */
   SNTL_PERSISTENCE_STANDALONE_DEVICE        = 1,
   SNTL_PERSISTENCE_NETWORK_DEVICE           = 2, /* Not Supported currently. */
   SNTL_PERSISTENCE_STANDALONE_CUSTOM_DEVICE = 3, /* Not Supported currently. */
   SNTL_PERSISTENCE_NETWORK_CUSTOM_DEVICE    = 4  /* Not Supported currently. */
};

typedef enum sntl_persistence_device sntl_persistence_device_t;

/*! \brief          Creates the Persistence Context object.
*
* \param            device,   [in]  Target device type.
* \param            attr,     [in]  The (optional) attribute object.
* \param            context   [out] Points to the persistence context 
*                                   object created. Memory resources 
*                                   shall be allocated by the API and 
*                                   can be released using 
*                                   sntl_persistence_context_delete().
*
* \return           SNTL_PERSISTENCE_SUCCESS if successful, otherwise, 
*                   an appropriate error code.
*
* \remark           For further information, please refer to the '
*                   API Reference Guide' document.
*/
SNTL_DECLARE(sntl_persistence_status_t) sntl_persistence_context_new(
                                           sntl_persistence_device_t    device,
                                           sntl_persistence_attr_t     *attr,
                                           sntl_persistence_context_t **context);

/*! \brief          Deletes the Persistence Context object.
*
* \param            context    [in] The persistence context object to
*                                   be deleted.
*
* \return           SNTL_PERSISTENCE_SUCCESS if successful, otherwise, 
*                   an appropriate error code.
*
* \remark           For further information, please refer to the 
*                   'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_persistence_status_t) sntl_persistence_context_delete(
                                             sntl_persistence_context_t *context);

/*! \brief          Performs Persistence initialization or creation.
*
* \param            context    [in] The persistence context object.
* \param            input      [in] Currently unused.
*
* \return           SNTL_PERSISTENCE_SUCCESS if successful, otherwise, 
*                   an appropriate error code.
*
* \remark           For further information, please refer to the 
*                   'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_persistence_status_t) sntl_persistence_create(
                                           sntl_persistence_context_t *context,
                                           char                       *input);

/*! \brief          Gets detailed error information related to errors
*                   encountered in persistence API's, i.e.
*                   (sntl_persistence_create)
*
* \param            context   [in] The persistence context object
* \param            scope     [in] Currently not supported.
* \param            query     [in] Currently,query supported is 
*                                  "SNTL_PRS_QUERY_ERR_INFO_LATEST"
* \param            info      [out] Pointer to the buffer containing
*                                   XML-based output. Memory resources 
*                                   shall be allocated by the API and 
*                                   can be released using sntl_persistence_free().
*
* \return           SNTL_PERSISTENCE_SUCCESS if successful,
*                    otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*                   'API Reference Guide' document.
*
*/
SNTL_DECLARE(sntl_persistence_status_t) sntl_persistence_get_info
(
    sntl_persistence_context_t *context,
    const char *scope,
    const char *query,
    char **info
);

/*! \brief          Release memory resources allocated in sntl_persistence_get_info API.
*
* \param            buffer       [in] Pointer to the buffer containing XML-based output.
*
* \return           void
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*
*/
SNTL_DECLARE(void) sntl_persistence_free(void *buffer);

/*! \brief          Performs persistence library level cleanup.
*
* \return           SNTL_PERSISTENCE_SUCCESS if successful, otherwise, 
*                   an appropriate error code.
*
* \remark           For further information, please refer to the 
*                   'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_persistence_status_t) sntl_persistence_cleanup(void);

//XML tags related to sntl_persistence_get_info API
#define SNTL_PRS_QUERY_ERR_INFO_VERSION(v)        "<persistenceQuery query=\"lastErrorInfo\" version=\"" v "\"/>"
#define SNTL_PRS_QUERY_ERR_INFO_LATEST            SNTL_PRS_QUERY_ERR_INFO_VERSION("1.0")

#ifdef __cplusplus
} // extern "C"
#endif

#endif /* #define _LSPMGMTINIT_H */

/*End of File */
