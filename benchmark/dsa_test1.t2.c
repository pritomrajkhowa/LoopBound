extern void __VERIFIER_error() __attribute__ ((__noreturn__));
void __VERIFIER_assert(int cond) { if(!(cond)) { ERROR: __VERIFIER_error(); } }
int __VERIFIER_nondet_int();
int main() {
int v1 = __VERIFIER_nondet_int();
int v2 = __VERIFIER_nondet_int();
goto loc2;
loc2:
 if (__VERIFIER_nondet_int()) {
  goto loc0;
 }
 goto end;
loc0:
 if (__VERIFIER_nondet_int()) {
  v1 = __VERIFIER_nondet_int();
  v2 = __VERIFIER_nondet_int();
  goto loc1;
 }
 goto end;
loc1:
end:
;
}
