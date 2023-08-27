(defparameter m (make-hash-table))

(dotimes (i 101)
   (dotimes (j 101)
     (if (> i 1)
         (if (> j 1)
           (setf (gethash (expt i j) m) (expt i j) 
       )))))

(print (hash-table-count m))
