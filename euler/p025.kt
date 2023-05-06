import java.math.BigInteger
fun main(args: Array<String>) {
  var a = BigInteger("1")
  var b = BigInteger("1")
  var i = BigInteger("2")
  while (b.toString().length < 1000) {
    val b_old = b
    b = a.add(b)
    a = b_old
    i = i.add(BigInteger("1"))
  }
  println(i)
}
