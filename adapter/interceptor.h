/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * Distributed under BSD 3-Clause license.                                   *
 * Copyright by The HDF Group.                                               *
 * Copyright by the Illinois Institute of Technology.                        *
 * All rights reserved.                                                      *
 *                                                                           *
 * This file is part of Hermes. The full Hermes copyright notice, including  *
 * terms governing use, modification, and redistribution, is contained in    *
 * the COPYING file, which can be found at the top directory. If you do not  *
 * have access to the file, you may request a copy from help@hdfgroup.org.   *
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

#ifndef HERMES_ADAPTER_UTILS_H_
#define HERMES_ADAPTER_UTILS_H_

#include "hermes.h"
#include "adapter/filesystem/filesystem_mdm.h"
#include "adapter/filesystem/filesystem_mdm_singleton_macros.h"

namespace stdfs = std::experimental::filesystem;

namespace hermes::adapter {

#define HERMES_DECL(F) F

/** The maximum length of a POSIX path */
static inline const int kMaxPathLen = 4096;


/** get the file name from \a fp file pointer */
inline std::string GetFilenameFromFP(FILE* fp) {
  char proclnk[kMaxPathLen];
  char filename[kMaxPathLen];
  int fno = fileno(fp);
  snprintf(proclnk, kMaxPathLen, "/proc/self/fd/%d", fno);
  size_t r = readlink(proclnk, filename, kMaxPathLen);
  filename[r] = '\0';
  return filename;
}

}  // namespace hermes::adapter

#endif  // HERMES_ADAPTER_UTILS_H_
