/*******************************************************************/
/*                                                                 */
/*               Copyright (C) 2021 Thales Group                   */
/*                      All Rights Reserved.                       */
/*                                                                 */
/*     This Module contains Proprietary Information of Thales      */
/*          Group, and should be treated as Confidential.          */
/*******************************************************************/

/**
 * \mainpage Sentinel License parse API
 * \file licgen_parse.h Sentinel Licensing API declarations
 */




#ifndef SNTL_LICGEN_H
#define SNTL_LICGEN_H

/* H****************************************************************
* FILENAME    : licgen_parser.h
*
* DESCRIPTION :
*           Contains public function prototypes, macros and defines
*           need for license parse using Sentinel Developer Kit.
* USAGE       :
*           This file should be included for the sntl APIs related to license parse functionality
*
*H*/

#ifdef __cplusplus
extern "C" {
#endif


/**
* @defgroup Macros, typedefs Sentinel Types and Status Codes
* @{
*/

#define SNTL_LICGEN_DECLARE(_type)                _type

/* This defines the maximum length of a license string */
#define SNTL_LICGEN_MAX_LICENSE_SIZE           6400
/*! Sentinel Status Codes */
enum sntl_licgen_status_codes
{
 /* Success */ 
 SNTL_LICGEN_SUCCESS=0,     
 /*License string's length is greater than supported length */
 SNTL_LICGEN_EXCEEDS_MAX_STRLEN = 310006, 
  /*License string contains invalid characters*/
 SNTL_LICGEN_INVALID_CHARS = 310016,
 /* License string's length is smaller than supported length */ 
 SNTL_LICGEN_SHORT_STRING = 310017,
 /* Premature termination of license code due to intermediate error */
 SNTL_LICGEN_PREMATURE_TERM = 310018,
 /* Failed to remap default strings from configuration file for license */
 SNTL_LICGEN_REMAP_DEFAULT = 310019,
 /* Decryption failed for license code.*/
 SNTL_LICGEN_DECRYPT_FAIL = 310020,
 /* Checksum validation failed for license code Please verify the license code. */
 SNTL_LICGEN_INVALID_CHKSUM = 310022,
 /* Default fixed string error. */
 SNTL_LICGEN_FIXED_STR_ERROR = 310023,
 /*Decryption failed for secrets. Verify the configuration file for readable licenses. */
 SNTL_LICGEN_SECRET_DECRYPT_FAILURE = 310024,
 /* Error in license string. Please check. */ 
 SNTL_LICGEN_SIMPLE_ERROR = 310025,
 /*Out of heap memory.*/
 SNTL_LICGEN_MALLOC_FAILURE = 310026,
  /*Generic error while performing the license parse operations*/ 
 SNTL_LICGEN_INTERNAL_ERROR = 310027,
  /*If invalid input is given.*/
 SNTL_LICGEN_INVALID_INPUT = 310030,
  /*Maximum limit crossed.*/
 SNTL_LICGEN_MAX_LIMIT_CROSSED = 310031,
  /*No resources left.*/
 SNTL_LICGEN_NO_RESOURCES = 310032,
  /*Bad file handle.*/
 SNTL_LICGEN_BAD_HANDLE = 310033,
  /*Operation failed.*/
 SNTL_LICGEN_FAIL  = 310034,
  /*Vendor identification is not valid.*/
 SNTL_LICGEN_INVALID_VENDOR_CODE  = 310035,
  /*Vendor-customized encryption failed.*/
 SNTL_LICGEN_VENDOR_ENCRYPTION_FAIL  = 310036,
   /*
    * RMS Development Kit LicenseMeter related error codes.
    */
 /*Unknown exception in accessing Sentinel RMS license meter(s).*/	
 SNTL_LICGEN_LICMETER_EXCEPTION  = 310040,
 /* Error in updating locale. */
 SNTL_LICGEN_VI18N_INITIALIZE_FAIL = 310059,   
   /* Your license meter is not supported. */
 SNTL_LICGEN_LICMETER_NOT_SUPPORTED = 310070, 
 /* Process fail to acquire the lock  */
 SNTL_LICGEN_GETLOCK_FAIL = 310077,
  /* Process lock request time-out.  */  
 SNTL_LICGEN_GETLOCK_TIMEOUT = 310078,
  /* Vendor decryption failed. */
 SNTL_LICGEN_VENDOR_DECRYPTION_FAIL = 310079,
};
typedef enum sntl_licgen_status_codes sntl_licgen_status_t;

/*! \brief      Parse the license string and generate the XML output based on available attributes in the license string.
*
* \param        licgen_context [in] The license generator context object for the future purpose. For now It will always be NULL 
* \param        input         [in] The input license string to be parsed 
* \param        info          [out] The parsed XML output license string after parse. 
* \return       SNTL_LICGEN_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark       For further information, Please refer the RMS SDK API reference guide
*/
SNTL_LICGEN_DECLARE(sntl_licgen_status_t) sntl_licgen_parse(void* licgen_context,
                                const char *input,                               
                                char **info);
								

/*! \brief     Frees the memory resources allocated to storing retrieved data from API calls. 
*
* \param       buffer      [in] Pointer to the memory resources allocated by any of the following APIs:
* \return      SNTL_LICGEN_SUCCESS if successful, otherwise, an appropriate error code.
*
* \remark      For further information, Please refer the RMS SDK API reference guide
*/
SNTL_LICGEN_DECLARE (void) sntl_licgen_free(void *buffer);
#ifdef __cplusplus
} // extern "C"
#endif

#endif /* #define SNTL_LICGEN_H */

/*End of File */

