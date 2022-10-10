// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

// DO NOT EDIT THIS FILE. Update from pyarrow/lib.h after pyarrow build

/* Generated by Cython 0.29.15 */

#ifndef __PYX_HAVE__pyarrow__lib
#define __PYX_HAVE__pyarrow__lib

#include "Python.h"

#ifndef __PYX_HAVE_API__pyarrow__lib

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#ifndef DL_IMPORT
  #define DL_IMPORT(_T) _T
#endif

__PYX_EXTERN_C PyObject *__pyx_f_7pyarrow_3lib_pyarrow_wrap_scalar(std::shared_ptr< arrow::Scalar>  const &);
__PYX_EXTERN_C PyObject *__pyx_f_7pyarrow_3lib_pyarrow_wrap_array(std::shared_ptr< arrow::Array>  const &);
__PYX_EXTERN_C PyObject *__pyx_f_7pyarrow_3lib_pyarrow_wrap_chunked_array(std::shared_ptr< arrow::ChunkedArray>  const &);
__PYX_EXTERN_C PyObject *__pyx_f_7pyarrow_3lib_pyarrow_wrap_batch(std::shared_ptr< arrow::RecordBatch>  const &);
__PYX_EXTERN_C PyObject *__pyx_f_7pyarrow_3lib_pyarrow_wrap_buffer(std::shared_ptr< arrow::Buffer>  const &);
__PYX_EXTERN_C PyObject *__pyx_f_7pyarrow_3lib_pyarrow_wrap_data_type(std::shared_ptr< arrow::DataType>  const &);
__PYX_EXTERN_C PyObject *__pyx_f_7pyarrow_3lib_pyarrow_wrap_field(std::shared_ptr< arrow::Field>  const &);
__PYX_EXTERN_C PyObject *__pyx_f_7pyarrow_3lib_pyarrow_wrap_resizable_buffer(std::shared_ptr< arrow::ResizableBuffer>  const &);
__PYX_EXTERN_C PyObject *__pyx_f_7pyarrow_3lib_pyarrow_wrap_schema(std::shared_ptr< arrow::Schema>  const &);
__PYX_EXTERN_C PyObject *__pyx_f_7pyarrow_3lib_pyarrow_wrap_table(std::shared_ptr< arrow::Table>  const &);
__PYX_EXTERN_C PyObject *__pyx_f_7pyarrow_3lib_pyarrow_wrap_tensor(std::shared_ptr< arrow::Tensor>  const &);
__PYX_EXTERN_C PyObject *__pyx_f_7pyarrow_3lib_pyarrow_wrap_sparse_coo_tensor(std::shared_ptr< arrow::SparseCOOTensor>  const &);
__PYX_EXTERN_C PyObject *__pyx_f_7pyarrow_3lib_pyarrow_wrap_sparse_csr_matrix(std::shared_ptr< arrow::SparseCSRMatrix>  const &);
__PYX_EXTERN_C PyObject *__pyx_f_7pyarrow_3lib_pyarrow_wrap_sparse_csc_matrix(std::shared_ptr< arrow::SparseCSCMatrix>  const &);
__PYX_EXTERN_C PyObject *__pyx_f_7pyarrow_3lib_pyarrow_wrap_sparse_csf_tensor(std::shared_ptr< arrow::SparseCSFTensor>  const &);
__PYX_EXTERN_C std::shared_ptr< arrow::Scalar>  __pyx_f_7pyarrow_3lib_pyarrow_unwrap_scalar(PyObject *);
__PYX_EXTERN_C std::shared_ptr< arrow::Array>  __pyx_f_7pyarrow_3lib_pyarrow_unwrap_array(PyObject *);
__PYX_EXTERN_C std::shared_ptr< arrow::ChunkedArray>  __pyx_f_7pyarrow_3lib_pyarrow_unwrap_chunked_array(PyObject *);
__PYX_EXTERN_C std::shared_ptr< arrow::RecordBatch>  __pyx_f_7pyarrow_3lib_pyarrow_unwrap_batch(PyObject *);
__PYX_EXTERN_C std::shared_ptr< arrow::Buffer>  __pyx_f_7pyarrow_3lib_pyarrow_unwrap_buffer(PyObject *);
__PYX_EXTERN_C std::shared_ptr< arrow::DataType>  __pyx_f_7pyarrow_3lib_pyarrow_unwrap_data_type(PyObject *);
__PYX_EXTERN_C std::shared_ptr< arrow::Field>  __pyx_f_7pyarrow_3lib_pyarrow_unwrap_field(PyObject *);
__PYX_EXTERN_C std::shared_ptr< arrow::Schema>  __pyx_f_7pyarrow_3lib_pyarrow_unwrap_schema(PyObject *);
__PYX_EXTERN_C std::shared_ptr< arrow::Table>  __pyx_f_7pyarrow_3lib_pyarrow_unwrap_table(PyObject *);
__PYX_EXTERN_C std::shared_ptr< arrow::Tensor>  __pyx_f_7pyarrow_3lib_pyarrow_unwrap_tensor(PyObject *);
__PYX_EXTERN_C std::shared_ptr< arrow::SparseCOOTensor>  __pyx_f_7pyarrow_3lib_pyarrow_unwrap_sparse_coo_tensor(PyObject *);
__PYX_EXTERN_C std::shared_ptr< arrow::SparseCSRMatrix>  __pyx_f_7pyarrow_3lib_pyarrow_unwrap_sparse_csr_matrix(PyObject *);
__PYX_EXTERN_C std::shared_ptr< arrow::SparseCSCMatrix>  __pyx_f_7pyarrow_3lib_pyarrow_unwrap_sparse_csc_matrix(PyObject *);
__PYX_EXTERN_C std::shared_ptr< arrow::SparseCSFTensor>  __pyx_f_7pyarrow_3lib_pyarrow_unwrap_sparse_csf_tensor(PyObject *);

#endif /* !__PYX_HAVE_API__pyarrow__lib */

/* WARNING: the interface of the module init function changed in CPython 3.5. */
/* It now returns a PyModuleDef instance instead of a PyModule instance. */

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC initlib(void);
#else
PyMODINIT_FUNC PyInit_lib(void);
#endif

#endif /* !__PYX_HAVE__pyarrow__lib */
