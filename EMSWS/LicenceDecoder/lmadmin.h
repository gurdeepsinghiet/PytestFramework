/*******************************************************************/
/*                                                                 */
/*               Copyright (C) 2021 Thales Group                   */
/*                      All Rights Reserved.                       */
/*                                                                 */
/*     This Module contains Proprietary Information of Thales      */
/*          Group, and should be treated as Confidential.          */
/*******************************************************************/

/**
 * \mainpage Sentinel Admin API
 * \file lmadmin.h Sentinel Admin API declarations
 */


#ifndef SNTL_LMADMIN_H
#define SNTL_LMADMIN_H

/* H****************************************************************
* FILENAME    : lmadmin.h
*
* DESCRIPTION :
*           Contains public function prototypes, macros and defines
*           needed for Administrating Sentinel RMS License Manager.
* USAGE       :
*           This file should be included by the developer who is 
*           creating applications that are being used to Administer
*           Sentinel RMS License Manager.
*
*H*/

#ifdef __cplusplus
extern "C" {
#endif

#define SNTL_LMADMIN_COPYRIGHT_STR    "  Copyright (C) 2021 Thales Group\n       All Rights Reserved.\n\n"

#define SNTL_LMADMIN_NULL 0
/**
* @defgroup Macros, typedefs Sentinel Types and Status Codes
* @{
*/


#define SNTL_DECLARE(_type)                _type

/*! Sentinel Status Codes */
enum sntl_lmadmin_status_codes
{
/*! The function executed successfully. */
   SNTL_LMADMIN_SUCCESS = 0,

/*! Library is already in initialized state. */
   SNTL_LMADMIN_LIBRARY_ALREADY_INITIALIZED = 410001,

/*! Failed to resolve the server host. */
   SNTL_LMADMIN_HOST_UNKNOWN = 410002,
   
/*! License server is not RUNNING. */
   SNTL_LMADMIN_NO_SERVER_RUNNING = 410003,

/*! The network is unavailable. */ 
   SNTL_LMADMIN_NO_NETWORK = 410004, 

/*! On the specified machine, license server is not responding.
 *  (Probable cause - network down, wrong port number, some other
 *  application on that port, etc.). */
   SNTL_LMADMIN_NO_SERVER_RESPONSE = 410005,

/*! TCPIP protocol version specified for lmadmin library is incorrect. */
   SNTL_LMADMIN_INVALID_TCPIP_VERSION = 410006,  

/*! Error in calling API. */
   SNTL_LMADMIN_CALLING_ERROR = 410007,
   
/*! Internal error in termination or accessing feature. */
   SNTL_LMADMIN_INTERNAL_ERROR = 410008,

/*! An error has occurred in decrypting (or decoding) a network message. */
   SNTL_LMADMIN_BAD_SERVER_MESSAGE = 410009,

/*! Library is not in initialized state. */
   SNTL_LMADMIN_LIBRARY_NOT_INITIALIZED = 410010,

/*! The requested operation is not supported on this license server. */
   SNTL_LMADMIN_NOT_SUPPORTED = 410011,
   
/*! Insufficient resources (such as memory) are available to complete the request. */
   SNTL_LMADMIN_NORESOURCES = 410012,   
   
/*! No more active keys are available for the cleanup. */
   SNTL_LMADMIN_CLEANUP_ERR_NOKEYS = 410013,
   
/*! Cleanup on server passed excluding cleanup for commuter/capacity keys. */
   SNTL_LMADMIN_DEL_SUCC_WITH_EXCLUSION = 410014, 
   
/*! Client not authorized to make the specified request. */
   SNTL_LMADMIN_CLIENT_NOT_AUTHORIZED = 410015,

/*! The feature is not supported in the No-Net mode. */
   SNTL_LMADMIN_NOT_SUPPORTED_IN_NONET_MODE = 410016,

/*! Fail to acquire API lock. API call should be re-tried on receiving this error. */
   SNTL_LMADMIN_RESOURCE_LOCK_FAILURE = 410017,

/*! Invalid Application Context. */
   SNTL_LMADMIN_INVALID_CONTEXT = 410018,

/*! Invalid Attribute Key. */
   SNTL_LMADMIN_INVALID_ATTR_KEY = 410019,

/*! Invalid Attribute Value. */
   SNTL_LMADMIN_INVALID_ATTR_VALUE = 410020

};

/*! Status type */
typedef unsigned int       sntl_lmadmin_uint32_t;

typedef enum sntl_lmadmin_status_codes sntl_lmadmin_status_t;

/*! Attribute */
typedef void sntl_lmadmin_attr_t;

/*! Admin Context */
typedef void sntl_lmadmin_context_t;

/**
* @defgroup attrib_related_APIs Attribute related APIs
* @{
*/

/**
* \brief            Creates a new attribute object.
*
* \param            attr      [out] Points to the attribute object created.
*   						  Memory resources shall be allocated by the API 
*							  and can be released using sntl_lmadmin_attr_delete().
*
* \return           SNTL_LMADMIN_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_lmadmin_status_t) sntl_lmadmin_attr_new(sntl_lmadmin_attr_t **attr);

/**
* \brief            Sets values in the attribute object.
*
* \param            attr      [in] The attribute object in which the "value" is to be set based on the "key".
* \param            key       [in] The "key" based on which "value" would be set.
*            e.g., SNTL_ATTR_LMADMINCONTEXT_NETWORK_TIMEOUT is one of the keys for an admin context object.
* \param            value     [in] The "value" to be set.
*            e.g., "30" can be a valid value for the key SNTL_ATTR_LMADMINCONTEXT_NETWORK_TIMEOUT.
*
* \return           SNTL_LMADMIN_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_lmadmin_status_t) sntl_lmadmin_attr_set(sntl_lmadmin_attr_t *attr,
                                                          const char *key,
                                                          const char *value);

/*! \brief          Deletes the attribute object.
*
* \param            attr      [in] The attribute object to be deleted.
*
* \return           SNTL_LMADMIN_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(void) sntl_lmadmin_attr_delete(sntl_lmadmin_attr_t *attr);

/**
* @defgroup config_APIs ADMIN Library Configuration API and Macros
* @{
*/
#define SNTL_ATTR_LMADMINCONFIG_TRACE_WRITER_FILE                   "lmadminconfig_trace_writer_file"
#define SNTL_ATTR_LMADMINCONFIG_TRACE_LEVEL                         "lmadminconfig_trace_level"

/* Possible values for attribute 'SNTL_ATTR_ADMINCONFIG_TRACE_LEVEL' used by the library. */
#define SNTL_ATTR_LMADMINCONFIG_TRACE_FUNCTION                "lmadmin_trace_function"
#define SNTL_ATTR_LMADMINCONFIG_TRACE_ERROR                   "lmadmin_trace_error"

/* Macros for setting attributes for sntl_lmadmin_configure(). */
#define sntl_lmadmin_attr_set_config_trace_writer_file(_attr, _value) \
sntl_lmadmin_attr_set(_attr, SNTL_ATTR_LMADMINCONFIG_TRACE_WRITER_FILE , _value)

/* SNTL_ATTR_LMADMINCONFIG_TRACE_FUNCTION SNTL_ATTR_LMADMINCONFIG_TRACE_ERROR */
#define sntl_lmadmin_attr_set_config_trace_level(_attr, _value) \
   sntl_lmadmin_attr_set(_attr, SNTL_ATTR_LMADMINCONFIG_TRACE_LEVEL, _value) 
   

/*! \brief      Performs admin library configuration defined by the attribute object parameter.
*
* \param        attr         [in] The attribute object.
*
* \return       SNTL_LMADMIN_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark       For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_lmadmin_status_t) sntl_lmadmin_configure(const sntl_lmadmin_attr_t *attr);

/**
* @defgroup admin_context_MACROs_APIs Admin Context related APIs and Macros
* @{
*/
#define SNTL_ATTR_LMADMINCONTEXT_NETWORK_TIMEOUT              "lmadmincontext_network_timeout"

#define sntl_lmadmin_attr_set_admincontext_timeout_interval(_attr, _value) \
   sntl_lmadmin_attr_set(_attr, SNTL_ATTR_LMADMINCONTEXT_NETWORK_TIMEOUT, _value)

/*! \brief          Creates the LM Admin Context object.
*
* \param            server_name,      [in]  contacted server name default localhost.
* \param            server_port,,     [in]  contacted server port
* \param            attr              [in]  The (optional) attribute object.
* \param            admin_context     [out] Points to the admin context object created.               
*                                  Memory resources shall be allocated by the API 
*                                  and can be released using sntl_lmadmin_context_delete().
*
*
* \return           SNTL_LMADMIN_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_lmadmin_status_t) sntl_lmadmin_context_new(const char *server_name,
                                                             unsigned int server_port,
                                                             sntl_lmadmin_attr_t *attr,
                                                             sntl_lmadmin_context_t **admin_context);

/*! \brief          Deletes the Admin Context object.
*
* \param            admin_context    [in] The admin context object to be deleted.
*
* \return           SNTL_LMADMIN_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_lmadmin_status_t) sntl_lmadmin_context_delete(sntl_lmadmin_context_t *admin_context);

/* Macros specifying the "query" parameter for sntl_lmadmin_get().
 */
#define SNTL_QUERY_LMADMIN_LIBRARY_INFO                           "<lmadminQuery query=\"libraryInfo\"/>"
 
#define SNTL_QUERY_LMADMIN_LIBRARY_INFO_VERSION(v)                "<lmadminQuery query=\"libraryInfo\" version=\"" v "\"/>"

/* Refer documentation for the supported versions. 
 */
#define SNTL_QUERY_LMADMIN_LIBRARY_INFO_LATEST                    SNTL_QUERY_LMADMIN_LIBRARY_INFO_VERSION("1.0")

/*! \brief      Retrieves information based on the "query" parameter passed.
*
* Based on the "query" parameter, the following types of information can be retrieved using this API:
*
*   libraryInfo
*
* \param        admin_context   [in] The admin context object. 
* \param        scope           [in] The "scope" for the "query" being made. Refer to the 'API Reference Guide' document for details.
* \param        query           [in] The "query" type, e.g., SNTL_QUERY_LMADMIN_LIBRARY_INFO.
* \param        info            [out] Pointer to the buffer containing XML-based output.
*                               Memory resources shall be allocated by the API and can be released using sntl_lmadmin_free().
*
* \return       SNTL_LMADMIN_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark       For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_lmadmin_status_t) sntl_lmadmin_get(sntl_lmadmin_context_t *admin_context,
                                                     const char *scope,
                                                     const char *query,
                                                     char **info);

/*! \brief      submits command/operation to be executed using the admin-context on targeted 
*               Sentinel RMS License Manager.
*
* Based on the "input" parameter, the following types of action can be performed using this API:
*
*   terminateUserSession
*
* \param        admin_context   [in] The admin context object. 
* \param        input           [in] Action and its required inputs. Refer to the 'API Reference Guide' document for details.
* \param        status          [out] XML return status for post API .
* \return       SNTL_LMADMIN_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark       For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_lmadmin_status_t) sntl_lmadmin_post(sntl_lmadmin_context_t *admin_context,
                                                      const char *input,
                                                      char **status);

/*! \brief     Frees the memory resources allocated to storing retrieved data from API calls. 
*
* \param       buffer      [in] Pointer to the memory resources allocated by any of the following APIs:
*   <ul>
*     <li>sntl_lmadmin_get()</li>
*   </ul>
* \return      This is a void function.
*
* \remark      For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(void) sntl_lmadmin_free(void *buffer);

/*! \brief          Performs admin library level cleanup.
*
* \return           SNTL_LMADMIN_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark           For further information, please refer to the 'API Reference Guide' document.
*/
SNTL_DECLARE(sntl_lmadmin_status_t) sntl_lmadmin_cleanup();


#ifdef __cplusplus
} // extern "C"
#endif

#endif /* #define SNTL_LMADMIN_H */