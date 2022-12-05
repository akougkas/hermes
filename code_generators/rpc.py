
"""
Automatically generate the RPCs for a series of Local functions

USAGE:
    cd code_generators/bin
    python3 rpc.py [modify=True]

modify: whether or not to modify actual source files.
"""

import sys
from code_generators.rpc.generator import RpcGenerator
from code_generators.util.paths import HERMES_ROOT

rpc_defs_path = f"{HERMES_ROOT}/src/rpc_thallium_defs.cc"
if len(sys.argv) < 2:
    gen = RpcGenerator(rpc_defs_path, True)
else:
    gen = RpcGenerator(rpc_defs_path, sys.argv[1])

gen.set_file(f"{HERMES_ROOT}/src/metadata_manager.h", "MetadataManager", "mdm")
gen.add("LocalGetOrCreateBucket", "rpc_->node_id_")
gen.add("LocalGetBucketId", "rpc_->node_id_")
gen.add("LocalBucketContainsBlob", "rpc_->node_id_")
gen.add("LocalRenameBucket", "rpc_->node_id_")
gen.add("LocalDestroyBucket", "rpc_->node_id_")
gen.add("LocalBucketPutBlob", "rpc_->node_id_")
gen.add("LocalGetBlobId", "rpc_->node_id_")
gen.add("LocalSetBlobBuffers", "rpc_->node_id_")
gen.add("LocalGetBlobBuffers", "rpc_->node_id_")
gen.add("LocalRenameBlob", "rpc_->node_id_")
gen.add("LocalDestroyBlob", "rpc_->node_id_")
gen.add("LocalWriteLockBlob", "rpc_->node_id_")
gen.add("LocalWriteUnlockBlob", "rpc_->node_id_")
gen.add("LocalReadLockBlob", "rpc_->node_id_")
gen.add("LocalReadUnlockBlob", "rpc_->node_id_")
gen.add("LocalGetOrCreateVBucket", "rpc_->node_id_")
gen.add("LocalGetVBucketId", "rpc_->node_id_")
gen.add("LocalUnlinkBlobVBucket", "rpc_->node_id_")
gen.add("LocalGetLinksVBucket", "rpc_->node_id_")
gen.add("LocalRenameVBucket", "rpc_->node_id_")
gen.add("LocalDestroyVBucket", "rpc_->node_id_")

gen.generate()