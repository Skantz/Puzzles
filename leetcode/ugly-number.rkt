(define/contract (is-ugly n)
  (-> exact-integer? boolean?)
    (cond
        [(< n 1) false]
        [(= n 1) true]
        [(= (modulo n 2) 0) (is-ugly (quotient n 2))]
        [(= (modulo n 3) 0) (is-ugly (quotient n 3))]
        [(= (modulo n 5) 0) (is-ugly (quotient n 5))]
        [true false]
    )
)
